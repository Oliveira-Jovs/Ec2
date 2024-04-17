import streamlit as st


def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def main():
    st.title("Verificador de Paridade")
    numero = st.number_input("Digite um número:", step=1)

    if st.button("Verificar"):
        resultado = verificar_paridade(numero)
        st.write(f"O número {numero} é {resultado}.")


if __name__ == "__main__":
    main()
