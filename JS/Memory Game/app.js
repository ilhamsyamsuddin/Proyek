document.addEventListener('DOMContentLoaded', () => {
    //card options
    const cardArray = [
        {
            name: 'C',
            img: 'images/C.png'
        },
        {
            name: 'C',
            img: 'images/C.png'
        },
        {
            name: 'Csharp',
            img: 'images/Csharp.png'
        },
        {
            name: 'Csharp',
            img: 'images/Csharp.png'
        },
        {
            name: 'C++',
            img: 'images/c++.png'
        },
        {
            name: 'C++',
            img: 'images/c++.png'
        },
        {
            name: 'html5',
            img: 'images/html5.png'
        },
        {
            name: 'html5',
            img: 'images/html5.png'
        },
        {
            name: 'java',
            img: 'images/java.png'
        },
        {
            name: 'java',
            img: 'images/java.png'
        },
        {
            name: 'JS',
            img: 'images/js.png'
        },
        {
            name: 'JS',
            img: 'images/js.png'
        }
    ]

cardArray.sort(() => 0.5- Math.random())

    const grid = document.querySelector('.grid')
    const resultDisplay = document.querySelector('#result')
    var cardChosen = []
    var cardChosenId = []
    const cardsWon = []
    //creating the board
    function createBoard(){
        for(let i=0;i<cardArray.length;i++){
            var card = document.createElement('img')
            card.setAttribute('src', 'images/blank.png')
            card.setAttribute('data-id', i)
            card.addEventListener('click',flipCard)
            grid.appendChild(card)
        }
    }
    //checking for match
    function checkForMatch(){
        var cards = document.querySelectorAll('img')
        const optionOneId = cardChosenId[0]
        const optionTwoId = cardChosenId[1]
        if(cardChosen[0] === cardChosen[1]){
            alert('You have found a match')
            cards[optionOneId].setAttribute('src', 'images/white.png')
            cards[optionTwoId].setAttribute('src', 'images/white.png')
            cards[optionOneId].removeEventListener('click', flipCard)
            cards[optionTwoId].removeEventListener('click', flipCard)
            cardsWon.push(cardChosen)
        }else{
            cards[optionOneId].setAttribute('src', 'images/blank.png')
            cards[optionTwoId].setAttribute('src', 'images/blank.png')
            alert('sorry, try again')
        }
        cardChosen = []
        cardChosenId = []
        resultDisplay.textContent = cardsWon.length
        if(cardsWon.length === cardArray.length/2){
            resultDisplay.textContent = "Congratulation!! You found them all"
        }

    }
    //flip the card
    function flipCard(){
        var cardId = this.getAttribute('data-id')
        cardChosen.push(cardArray[cardId].name)
        cardChosenId.push(cardId)
        this.setAttribute('src', cardArray[cardId].img)
        if(cardChosen.length === 2){
            setTimeout(checkForMatch,500)
        }
    }

    createBoard()
})