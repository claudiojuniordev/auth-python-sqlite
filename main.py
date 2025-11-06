from services.auth_service import register_user, login_user, list_users
from db import create_tables
import getpass

def main_menu():
    create_tables.create_tables() # garante que as tabelas existam

    while True:
        print("\n=== Sistema de Autenticação (Intermediário) ===")
        print("1 - Cadastrar usuário")
        print("2 - Autenticar usuário")
        print("3 - Listar usuários (dev)")
        print("4 - Sair")


        opcao = input("Escolha uma opção: ").strip()


        if opcao == "1":
            name = input("Nome: ").strip()
            login = input("Login: ").strip()
            senha = getpass.getpass("Senha: ")


            if not name or not login or not senha:
                print("Preencha todos os campos.")
                continue

            created = register_user(name, login, senha)
            if created:
                print("Usuário criado com sucesso.")
            else:
                print("Login já existe. Escolha outro login.")


        elif opcao == "2":
            identifier = input("Digite nome ou login: ").strip()
            senha = getpass.getpass("Senha: ")
            
            ok, nome = login_user(identifier, senha)
            if ok:
                print(f"Autenticado. Bem-vindo, {nome}.")
            else:
                print("Autenticação inválida.")

        elif opcao == "3":
            users = list_users()
            if not users:
                print("Nenhum usuário cadastrado.")
            else:
                print("--- Usuários (dev) ---")
            for u in users:
                print(f"{u['id']}: {u['name']} ({u['login']}) - criado em {u['created_at']}")


        elif opcao == "4":
            print("Encerrando.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main_menu()