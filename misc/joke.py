import koldstart


@koldstart.isolated("virtualenv", requirements=["pyjokes"])
def get_joke():
    import pyjokes

    return pyjokes.get_joke()
