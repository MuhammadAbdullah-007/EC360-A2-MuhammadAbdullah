from auth_service import register_user

def test_hash():
    assert register_user("a@b.com", "x")["hash"] != "x"
