import koldstart


@koldstart.cached
def prepare_model() -> int:
    return 42


@koldstart.isolated("virtualenv")
def run_stable_diffusion(prompt: str, iterations: int) -> bytes:
    model = prepare_model()
    return prompt.encode() * model * iterations
