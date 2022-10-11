const cardWrapperElem = document.getElementById("card-wrapper");
let cards = "";
for (let i = 0; i < 5; i++) {
  // `` 백틱(backtick) 안에서는 ${}를 통해서 javascript 변수를 사용할 수 있음.
  const cardElementHtml = `
        <div class='card'>Card - ${i + 1}</div>
    `;
  // 반복문을 돌면서 cards에 cardElementHtml을 계속 쌓는다.
  cards = cards + cardElementHtml;
}
// innerHTML 을 통해서 반복문을 통해 만들어진 cards를 cardWrapperEleme 안으로 넣는다.
cardWrapperElem.innerHTML = cards;
