window.onload = function () {
  const url = window.location.href;
  const elm = document.documentElement;
  const bottom = elm.scrollHeight - elm.clientHeight;

  if (url.includes('/detail') || url.includes('/message_result')) {
    // URLが '/detail'を含む場合(チャットルームに入ったとき)と'/message_result'を含む場合（メッセージ送信後）はページの最下部までスクロール
    window.scroll(0, bottom);
  } else {
    // 保存されていたスクロール位置があれば、そこまでスクロール
    const savedScrollPos = localStorage.getItem('scrollPos');
    if (savedScrollPos !== null) {
      window.scroll(0, savedScrollPos);
    }
  }
};

window.onbeforeunload = function () {
  // ページが '/detail'か'/message_result' でない場合だけスクロール位置を保存
  const url = window.location.href;
  if (!url.includes('/detail') && !url.includes('/message_result')) {
    const currentScrollPos = window.pageYOffset || document.documentElement.scrollTop;
    localStorage.setItem('scrollPos', currentScrollPos);
  }
};









