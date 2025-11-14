
            print('Academias Cadastradas!')
           
    def inserir_atetlas(self):
        cur = self.cursor()
        Atletas = [
            ('Lucas', '060.287.275-80', '22/06/1995', 'Leão', 'Preta', 64, 1, '07/11/2025'),
            ('Marcos', '415.982.134-09', '10/03/1990', 'Peixes', 'Roxa', 72, 1, '06/11/2025'),
            ('Juliana', '289.654.871-22', '15/08/1998', 'Leão', 'Azul', 58, 2, '05/11/2025'),
            ('Rafael', '301.875.640-51', '09/11/1993', 'Escorpião', 'Marrom', 82, 1, '03/11/2025'),
            ('Ana', '852.647.190-74', '27/04/2001', 'Touro', 'Branca', 56, 2, '01/11/2025'),
            ('Carlos', '164.920.387-33', '11/09/1988', 'Virgem', 'Preta', 95, 1, '30/10/2025'),
            ('Beatriz', '598.741.236-47', '20/01/2000', 'Aquário', 'Roxa', 62, 2, '29/10/2025'),
            ('Pedro', '715.834.209-10', '14/05/1996', 'Touro', 'Azul', 69, 1, '27/10/2025'),
            ('Camila', '947.162.508-25', '05/12/1994', 'Sagitário', 'Marrom', 60, 2, '26/10/2025'),
            ('Thiago', '328.756.941-62', '03/07/1992', 'Câncer', 'Preta', 88, 1, '25/10/2025'),
            ('Larissa', '419.385.270-13', '22/02/1999', 'Peixes', 'Azul', 57, 2, '24/10/2025'),
            ('Gabriel', '593.701.846-90', '17/10/1991', 'Libra', 'Roxa', 77, 1, '22/10/2025'),
            ('Renata', '230.894.561-22', '09/09/2002', 'Virgem', 'Branca', 54, 2, '21/10/2025'),
            ('Felipe', '672.580.193-48', '02/02/1995', 'Aquário', 'Preta', 81, 1, '19/10/2025'),
            ('Bruna', '809.315.467-72', '11/06/1997', 'Gêmeos', 'Marrom', 63, 2, '18/10/2025'),
            ('Victor', '736.904.582-60', '29/03/1990', 'Áries', 'Roxa', 70, 1, '16/10/2025'),
            ('Carolina', '905.781.423-17', '01/12/1998', 'Sagitário', 'Azul', 59, 2, '15/10/2025'),
            ('André', '154.392.708-45', '25/05/1993', 'Gêmeos', 'Preta', 85, 1, '14/10/2025'),
            ('Luiza', '268.541.907-83', '06/08/1999', 'Leão', 'Roxa', 61, 2, '13/10/2025'),
            ('Matheus', '497.630.815-29', '17/11/1994', 'Escorpião', 'Marrom', 79, 1, '12/10/2025'),
        ]

        sql_atletas = """

                INSERT INTO Atleta (nome, cpf, data_nascimento, equipe, faixa, peso, id_academia, data_inscricao)
                VALUES (?,?,?,?,?,?,?,?);

               """
        try:
            print("Inserindo Atletas....")
            print("////////....")
            cur.executemany( sql_atletas, Atletas)
        except sqlite3.Error as xy:
             print(f"\033[31mErro ao Cadastrar Atletas: {xy}\033[0m")
        finally:

            self.conn.commit()    
            print("Atletas Cadastrados!")
                    
    def mostrar_atletas(self):
        cur = self.cursor()
        cur.execute("SELECT * FROM Atleta;")
        
        categorias = cur.fetchall()
        
        if not categorias:
            print("\033[93mNenhum Atleta encontrado.\033[0m")  # amarelo
        else:
            print("\033[92m=== ATLETAS CADASTRADOS ===\033[0m")  # verde
            for cat in categorias:
                print(f"ID: {cat['id_atleta']} | Nome: {cat['nome']} | CPF: {cat['cpf']} | Data de Nascimento: {cat['data_nascimento']} | Equipe: {cat['equipe']} | Faixa: {cat['faixa']} | Peso: {cat['peso']}Kg | Academia: {cat['id_academia']} | Data Inscrição: {cat['data_inscricao']}     ")


    
    def limparDados(self):
            cur = self.cursor()
            cur.execute("DELETE FROM Academia;")
            cur.execute("DELETE FROM Lutas;")
            cur.execute("DELETE FROM Inscricoes;")
            cur.execute("DELETE FROM Atleta;")
            cur.execute("DELETE FROM sqlite_sequence WHERE name IN ('Atleta', 'Categoria', 'Lutas', 'Inscricoes');")

            print('DADOS LIMPOS')
