
const prompts = require('./prompts.js');
const keys = require('./keys.js');


function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

const functions = require("firebase-functions");

const admin = require("firebase-admin");
admin.initializeApp();

const dbRef = admin.firestore().doc("tokens/demo");

const TwitterAPI = require("twitter-api-v2").default;

const TwitterClient = new TwitterAPI({
  clientId: keys.clientId,
  clientSecret: keys.clientSecret,
});

const callbackURL =
  keys.callbackURL;

const { Configuration, OpenAIApi } = require("openai");
const configuration = new Configuration({
  organization: keys.organization,
  apiKey: keys.apiKey,
});
const openai = new OpenAIApi(configuration);

exports.auth = functions.https.onRequest(async (request, response) => {
  const { url, codeVerifier, state } = TwitterClient.generateOAuth2AuthLink(
    callbackURL,
    { scope: ["tweet.read", "tweet.write", "users.read", "offline.access"] }
  );

  await dbRef.set({ codeVerifier, state });
  response.redirect(url);
});

exports.callback = functions.https.onRequest(async (request, response) => {
  const { state, code } = request.query;

  const dbSnapshot = await dbRef.get();

  const { codeVerifier, state: storedState } = dbSnapshot.data();

  if (state !== storedState) {
    return response.status(400).send("Stored tokens dont match.");
  }

  const {
    client: loggedClient,
    accessToken,
    refreshToken,
  } = await TwitterClient.loginWithOAuth2({
    code,
    codeVerifier,
    redirectUri: callbackURL,
  });

  await dbRef.set({ accessToken, refreshToken });

  const { data } = await loggedClient.v2.me();

  response.send(data);
});

exports.tweet = functions.https.onRequest(async (request, response) => {
  const rnd = getRandomInt(prompts.length);
  const { refreshToken } = (await dbRef.get()).data();

  const {
    client: refreshedClient,
    accessToken,
    refreshToken: newRefreshToken,
  } = await TwitterClient.refreshOAuth2Token(refreshToken);

  await dbRef.set({ accessToken, refreshToken: newRefreshToken });
  
/*
  const nextTweet = await openai.createCompletion("text-davinci-001", {
    prompt: prompts[rnd],
    max_tokens: 64,
  });

  
  */
  const nextTweet = await openai.createCompletionFromModel({
    model: keys.mymodel,
    prompt: prompts[rnd],
    max_tokens:30
  });
  

  //testing
 
  const { data } = await refreshedClient.v2.tweet(
        nextTweet.data.choices[0].text
      );
    
      response.send(data);

  //response.send(nextTweet.data.choices[0].text);
  //firebase serve
});
