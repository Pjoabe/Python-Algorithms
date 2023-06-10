import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():

    assert encrypt_message("Hello World!", 2) == "!dlroW oll_eH"
    assert encrypt_message("Joabe Pereira", 7) == "P ebaoJ_ariere"
    assert encrypt_message("Saci Pererê", 6) == "êrere_P icaS"
    assert encrypt_message("Redline", 10) == "enildeR"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("ivalid", "key")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(13, 9)
