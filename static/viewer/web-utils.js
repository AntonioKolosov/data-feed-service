// @ts-nocheck
// Be interactions
// const BE_LOCATOR = 'http://127.0.0.1:8003' // local data-feed-service
const BE_LOCATOR = 'https://4a3b-129-159-137-238.ngrok-free.app'


// const WSS_LOCATOR = 'ws://127.0.0.1:8003' // local integrator
const WSS_LOCATOR = 'wss://4a3b-129-159-137-238.ngrok-free.app'

const url = `${WSS_LOCATOR}/ws`
const ws = new WebSocket(url);
// Get data
// ws.onmessage = function(event) {
//     // const subtitle = document.getElementById('play')
//     // const content = document.createTextNode(event.data)
//     const index = Number(event.data);
//     console.log(index)
//     messageIndex = index;
//     createNewMessage()
// };

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
