import replicate

def generate_moodboard(prompt):
    """Gera um moodboard com base na prompt fornecida."""
    # Chama o modelo Replicate para gerar o moodboard
    output = replicate.run(
        "black-forest-labs/flux-schnell",
        input={"prompt": prompt, "num_outputs": 4},
    )
    
    return output