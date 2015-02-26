(function() {
    "use strict";
    $(document).ready(function() {

        $('body').append('<canvas id="canvas" style="position:fixed;top:0;left:0;display:none;"></canvas>');

        //Canvas stuff
        var canvas = $("#canvas")[0];
        var ctx = canvas.getContext("2d");
        ctx.canvas.width = window.innerWidth;
        ctx.canvas.height = window.innerHeight;


        //Lets save the cell width in a variable for easy control
        var grid_size = 45;

        var cw = ctx.canvas.width / grid_size;
        var w = ctx.canvas.width - ctx.canvas.width % cw;
        var h = ctx.canvas.height - ctx.canvas.height % cw;
        var d;
        var food;
        var score;

        //Lets create the snake now
        var snake_array; //an array of cells to make up the snake

        var game_loop;

        var user_text = "";
        var coins_per_bite = 1;

//        $(document).on("keydown", function(e) {
//            if (e.which == 83) init();
//            return true;
//        });

        function init() {
            $("#mining_info_container").remove();
            $('body').append('<div id="mining_info_container"><p id="score"></p><p class="mining-rate">points gets you a coin!</p></div>')

            $('#snake-instructions').fadeIn('fast');
            setTimeout(function(){
                 $('#snake-instructions').fadeOut('fast');
            }, 4000);

            d = "right"; //default direction
            create_snake();
            create_food(); //Now we can see the food particle
            //finally lets display the score
            score = 0;

            $.ajaxSetup({
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
                    }
                }
            });

            $.get('/coin/award-point/')
                .done(function(data) {
                    score = data.points;
                    $(".mining-rate").prepend(data.ppc + " ");
                    $("#score").html("Score: <strong>" + score + "</strong>");
                });

            //Lets add the keyboard controls now
            $(document).on("keydown.snakeGame", function(e) {
                var key = e.which;
                //We will add another clause to prevent reverse gear
                if (key == "37" && d != "right") d = "left";
                else if (key == "38" && d != "down") d = "up";
                else if (key == "39" && d != "left") d = "right";
                else if (key == "40" && d != "up") d = "down";
                //The snake is now keyboard controllable

                if (key == 27) {
                    deInit();
                }

                if ($.inArray(key, [33, 34, 35, 36, 37, 38, 39, 40]) > -1) {
                    e.preventDefault();
                    return false;
                }

                return true;
            });

            $(canvas).show();

            //Lets move the snake now using a timer which will trigger the paint function
            //every 60ms
            if (typeof game_loop != "undefined") clearInterval(game_loop);
            game_loop = setInterval(paint, 100);
        }

        function create_snake() {
            var length = 5; //Length of the snake
            snake_array = []; //Empty array to start with
            for (var i = length - 1; i >= 0; i--) {
                //This will create a horizontal snake starting from the top left
                snake_array.push({
                    x: i,
                    y: 0
                });
            }
        }

        //Lets create the food now
        function create_food() {
            food = {
                x: Math.round(Math.random() * (w - cw) / cw),
                y: Math.round(Math.random() * (h - cw) / cw)
            };
            //This will create a cell with x/y between 0-44
            //Because there are 45(450/10) positions accross the rows and columns
        }

        //Lets paint the snake now
        function paint() {
            //To avoid the snake trail we need to paint the BG on every frame
            //Lets paint the canvas now
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            //        ctx.fillStyle = "rgba(0,0,0,0)";
            //        ctx.fillRect(0, 0, w, h);
            ctx.strokeStyle = "black";
            //ctx.strokeRect(0, 0, w, h);

            //The movement code for the snake to come here.
            //The logic is simple
            //Pop out the tail cell and place it infront of the head cell
            var nx = snake_array[0].x;
            var ny = snake_array[0].y;
            //These were the position of the head cell.
            //We will increment it to get the new head position
            //Lets add proper direction based movement now
            if (d == "right") nx++;
            else if (d == "left") nx--;
            else if (d == "up") ny--;
            else if (d == "down") ny++;

            //Lets add the game over clauses now
            //This will restart the game if the snake hits the wall
            //Lets add the code for body collision
            //Now if the head of the snake bumps into its body, the game will restart
            if (check_collision(nx, ny, snake_array)) {
                //restart game
                init();
                //Lets organize the code a bit now.
                return;
            }

            if (ny == h / cw) {
                ny = 0;
            } else if (ny == -1) {
                ny = h / cw;
            }

            if (nx == w / cw) {
                nx = 0;
            } else if (nx == -1) {
                nx = w / cw;
            }


            //Lets write the code to make the snake eat the food
            //The logic is simple
            //If the new head position matches with that of the food,
            //Create a new head instead of moving the tail
            if (nx == food.x && ny == food.y) {
                var tail = {
                    x: nx,
                    y: ny
                };
                //Create new food
                create_food();

                $.post('/coin/award-point/', { t:"somestupidshit" })
                    .done(function(data) {
                        if (data.cheater) {
                            sweetAlert({
                                title: "CHEATER!",
                                text: "Obviously the honor system doesn’t pertain to you, so you don’t get to mine anymore.",
                                type: "error",
                                confirmButtonColor: "#DD6B55",
                                confirmButtonText: "I suck"
                            }, function(){
                                window.location.href = "http://www.scientology.org/";
                            });
                        } else {
                            score = data.points;
                            $("#score").html("Score: <strong>" + score + "</strong>");
                            if (data.award) {
                                awardCoin();
                            }
                        }
                    });
            } else {
                var tail = snake_array.pop(); //pops out the last cell
                tail.x = nx;
                tail.y = ny;
            }
            //The snake can now eat the food.

            snake_array.unshift(tail); //puts back the tail as the first cell

            for (var i = 0; i < snake_array.length; i++) {
                var c = snake_array[i];
                //Lets paint 10px wide cells
                paint_cell(c.x, c.y);
            }

            //Lets paint the food
            paint_cell(food.x, food.y);




        }

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        function awardCoin() {
            var currentCoins = parseInt($('#coin_count').text().replace(',',''));
            console.log(currentCoins);
            $('#coin_count').text((currentCoins + 1).toLocaleString());
            var plusOne = $('<div id="plus_one">+1</div>');
            $('body').append(plusOne);
            plusOne.animate({
                opacity: 0.0,
                bottom: 270
            }, 2000, function() {
                $(this).remove();
            });
        }

        //Lets first create a generic function to paint cells
        function paint_cell(x, y) {
            ctx.fillStyle = "blue";
            ctx.fillRect(x * cw, y * cw, cw, cw);
            ctx.strokeStyle = "white";
            ctx.strokeRect(x * cw, y * cw, cw, cw);
        }

        function check_collision(x, y, array) {
            //This function will check if the provided x/y coordinates exist
            //in an array of cells or not
            for (var i = 0; i < array.length; i++) {
                if (array[i].x == x && array[i].y == y)
                    return true;
            }
            return false;
        }

        var deInit = function() {
            $(document).off(".snakeGame");
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            $(canvas).hide();
            clearInterval(game_loop);
            $("#mining_info_container").remove();
        };

        window.startSnake = init;

        window.stopSnake = deInit;
    });
})();