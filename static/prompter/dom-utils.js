// @ts-nocheck
// Create regular message
const createChatMessageElement = (message, id) => `
    <div class="message multiline" id=${id}>
    <div class="message-text">${message}</div>
    </div>
`
// Add top margin for shift to the bottom
const doMessageFirst = (index) => {
	const mess = document.querySelector(`#message${index}`)
	mess.classList.add('first-message') 
}

const doMessageCurrent = (currentMessageIndexShift) => {
	const chatMessages = document.querySelector('#chat-messages');
	const messagesLength = chatMessages.childElementCount;
	console.log("messagesLength", messagesLength);

	if ((messagesLength > currentMessageIndexShift)) {
		// Do the message font large and change background
		const curMess = chatMessages.children[messagesLength - (currentMessageIndexShift + 1)];
		curMess.classList.add('current-message');

		// Do the message font normal and restore background
		if (messagesLength > (currentMessageIndexShift + 1)) {
			const mess = chatMessages.children[messagesLength - (currentMessageIndexShift + 2)];
			mess.classList.remove('current-message');
		}
	}
};

