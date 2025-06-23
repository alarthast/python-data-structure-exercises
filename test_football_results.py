def test_output(capsys):
    from football_results import main

    main()
    captured = capsys.readouterr()
    assert captured.out == (
        "There were 6 matches in the group\n"
        "The match with the most goals was Hungary vs Portugal\n"
        "The match with the fewest goals was Portugal vs Austria\n"
        "The team(s) with the most total goals was Hungary\n"
        "The team(s) with the fewest total goals was Austria\n"
        "The team(s) with the most points was Hungary, Iceland\n"
        "The team(s) with the fewest points was Austria\n"
        "-------------------------\n"
        "Team      |G |W |D |L |P\n"
        "-------------------------\n"
        "Austria   |1 |0 |1 |2 |1 \n"
        "Hungary   |6 |1 |2 |0 |5 \n"
        "Portugal  |4 |0 |3 |0 |3 \n"
        "Iceland   |4 |1 |2 |0 |5 \n"
    )
