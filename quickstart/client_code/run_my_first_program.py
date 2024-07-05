from nada_ds import Party, SecretInteger, Input, Output

def nada_main():
    # Create a party
    party1 = Party(name="Party1")

    # Define secret integers from inputs
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform computation (multiplication in this case)
    result = my_int1 * my_int2

    # Return the result as output
    return [Output(result, "my_output", party1)]
