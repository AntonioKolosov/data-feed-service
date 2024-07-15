// @ts-nocheck
// Be interactions
// const BE_LOCATOR = '127.0.0.1:8003' // local data-feed-service
const BE_LOCATOR = 'data-feed-service.onrender.com'

// Get data from backend
async function fetchData(lang = 'ru') {
  const url = `https://${BE_LOCATOR}/webdata/${lang}`;
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

// Push data to backend
async function sendMessageIndex(index) {
  const url = `https://${BE_LOCATOR}/push/`+index;
  const response = await fetch(url);
  if (response.ok) {
      return {}
  } else {
      alert(response.status);
      return {}
  }
}
