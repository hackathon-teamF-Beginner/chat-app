// モーダルを表示させる

const addChannelModal = document.getElementById("add-channel-modal");
const deleteChannelModal = document.getElementById("delete-channel-modal");

const addPageButtonClose = document.getElementById("add-page-close-btn");
const deletePageButtonClose = document.getElementById("delete-page-close-btn");

const addChannelBtn = document.getElementById("add-channel-btn");

const addChannelConfirmBtn = document.getElementById(
  "add-channel-confirmation-btn"
);
const deleteChannelConfirmBtn = document.getElementById(
  "delete-channel-confirmation-btn"
);

// モーダルを開く
// <button id="add-channel-btn">チャンネル追加</button>ボタンがクリックされた時
addChannelBtn.addEventListener("click", () => {
  modalOpen("add");
});

function modalOpen(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "block";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "block";
  } else if (mode === "update") {
    updateChannelModal.style.display = "block";
  }
}

// モーダル内のバツ印がクリックされた時
addPageButtonClose.addEventListener("click", () => {
  modalClose("add");
});
deletePageButtonClose.addEventListener("click", () => {
  modalClose("delete");
});

function modalClose(mode) {
  if (mode === "add") {
    addChannelModal.style.display = "none";
  } else if (mode === "delete") {
    deleteChannelModal.style.display = "none";
  } else if (mode === "update") {
    updateChannelModal.style.display = "none";
  }
}

// モーダルコンテンツ以外がクリックされた時
addEventListener("click", outsideClose);
function outsideClose(e) {
  if (e.target == addChannelModal) {
    addChannelModal.style.display = "none";
  } else if (e.target == deleteChannelModal) {
    deleteChannelModal.style.display = "none";
  }
}



const reactionButton = document.getElementById('reaction-button');
const reactionModal = document.getElementById('reaction-modal');
const reactionOptions = document.getElementsByClassName('reaction-option');

// Show the modal when hovering over the reaction button
reactionButton.addEventListener('mouseover', function() {
  reactionModal.style.display = 'block';
});

// Hide the modal when a reaction is chosen
for(let i = 0; i < reactionOptions.length; i++) {
  reactionOptions[i].addEventListener('click', function() {
    reactionModal.style.display = 'none';
    // You can also do something with the chosen reaction here
    console.log("Reaction chosen: " + this.textContent);
  });
}

// Optionally, you could also hide the modal when the mouse leaves the modal area
reactionModal.addEventListener('mouseleave', function() {
  reactionModal.style.display = 'none';
});
