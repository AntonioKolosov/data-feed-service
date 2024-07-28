// @ts-nocheck
// Be interactions
// const BE_LOCATOR = 'http://127.0.0.1:8003' // local data-feed-service
const BE_LOCATOR = 'SESSION-GENERATED-URL'


// const WSS_LOCATOR = 'ws://127.0.0.1:8003' // local data-feed-service
const WSS_LOCATOR = 'SESSION-GENERATED-TCP-ADDRESS'

const url = `${WSS_LOCATOR}/ws`
const ws = new WebSocket(url);

// Get data from backend
async function fetchData(lang = 'ru') {
  const url = `${BE_LOCATOR}/webdata/${lang}`;
  const response = await fetch(url);
  if (response.ok) {
      const result = await response.json();  
      // now do something with the result
      // console.log("RESULT", result);
      return result
  } else {
      alert(response.status);
      return {}
  }
}
