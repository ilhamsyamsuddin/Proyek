document.addEventListener('DOMContentLoaded', ()=> {
    const squares = document.querySelectorAll('.grid div')
    const result = document.querySelector('#result')
    const displayCurrentPlayer = document.querySelector('#current-player')
    let currentPlayer = 1

    for(var i=0, len = squares.length; i< len; i++)

    (
        function(index){
            //add onclick to each squares
            squares[i].onclick = function(){
                //if the squares below your current square is taken, take the current square
                if(squares[index+7].classList.contains('taken')){
                    if(currentPlayer === 1){
                        squares[index].classList.add('taken')
                        squares[index].classList.add('player-one')
                        //change the player
                        currentPlayer = 2
                        displayCurrentPlayer.innerHTML = currentPlayer                       
                    }else if(currentPlayer===2){
                        squares[index].classList.add('taken')
                        squares[index].classList.add('player-two')
                        //change the player
                        currentPlayer = 1
                        displayCurrentPlayer.innerHTML = currentPlayer
                    }
                    //if the square below it is not taken, it is forbidden
                }else alert('cant go here')
            }
        }
    )
})(i)