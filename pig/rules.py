class Rules:
    """
    To win a game of pig you have to be the first to score 100 points,
    but you have to follow these rules:
    * You may roll until you get a single 1 or a double 1
        * If you roll a single 1 you lose your turn total and your turn ends
        * If you roll a double 1 your entire score is lost and your turn ends

    * You can decide to hold if you want to end your turn
        * If you decide to hold your turn total is added to your score
        * If you roll a double of any numbers except 1
        you are NOT allowed to hold until you have rolled again

    * The turn total is calculated by adding the number from each dice rolled
    together except 1

    * You have the option to cheat your way to victory,
    but you can't cheat your way to the top highscore
    """
