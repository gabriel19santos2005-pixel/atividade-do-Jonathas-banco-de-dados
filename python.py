import sqlite3
conn = sqlite3.connect("loja_select.db")
cursor = conn.cursor()
# Remover tabelas antigas, caso existam
cursor.execute("DROP TABLE IF EXISTS venda")
cursor.execute("DROP TABLE IF EXISTS produto")
cursor.execute("DROP TABLE IF EXISTS cliente")
# Criar tabela cliente
cursor.execute("""
CREATE TABLE cliente (
id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
cidade TEXT NOT NULL
)
""")
# Criar tabela produto
cursor.execute("""
CREATE TABLE produto (
id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
preco REAL NOT NULL,
estoque INTEGER NOT NULL
)
""")
# Criar tabela venda
cursor.execute("""
CREATE TABLE venda (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
id_cliente INTEGER NOT NULL,
valor REAL NOT NULL,
data_venda TEXT NOT NULL,
FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
)
""")
# Inserir clientes
clientes = [
("Ana Silva", "Macapá"),
("Bruno Costa", "Santana"),
("Carlos Almeida", "Macapá"),
("Mariana Souza", "Belém"),
("João Silva", "Santana"),
("Fernanda Lima", "Macapá"),
("Amanda Rocha", "Belém"),
("Pedro Martins", "Oiapoque"),
("Lucas Ferreira", "Macapá"),
("Aline Santos", "Santana")
]
cursor.executemany("""
INSERT INTO cliente (nome, cidade)
VALUES (?, ?)
""", clientes)
# Inserir produtos
produtos = [
("Notebook Dell", 3500.00, 8),
("Mouse Gamer", 120.00, 25),
("Teclado Mecânico", 280.00, 15),
("Monitor 24 Polegadas", 900.00, 6),
("Cabo HDMI", 35.00, 50),
("Headset Bluetooth", 180.00, 12),
("Mousepad Grande", 45.00, 30),
("Memória RAM 8GB", 250.00, 10),
("SSD 480GB", 320.00, 4),
("Webcam Full HD", 210.00, 7),
("Microfone USB", 450.00, 3),
("Carregador Universal", 85.00, 18)
]

cursor.executemany("""
INSERT INTO produto (nome, preco, estoque)
VALUES (?, ?, ?)
""", produtos)
# Inserir vendas
vendas = [
(1, 3500.00, "2026-05-01"),
(2, 120.00, "2026-05-02"),
(3, 900.00, "2026-05-03"),
(1, 280.00, "2026-05-04"),
(5, 35.00, "2026-05-05"),
(6, 180.00, "2026-05-06"),
(7, 320.00, "2026-05-07"),
(8, 450.00, "2026-05-08")
]
cursor.executemany("""
INSERT INTO venda (id_cliente, valor, data_venda)
VALUES (?, ?, ?)
""", vendas)
conn.commit()

query_clientes = cursor.execute("""SELECT * FROM cliente""")
print("Todos os clientes",query_clientes.fetchall())
print("")

query_produtos = cursor.execute("""SELECT * FROM produto""")
print("Todos os produtos",query_produtos.fetchall())
print("")

query_produto1 = cursor.execute("""SELECT nome, preco FROM produto;""")
print("Nomes,preços e produtos ",query_produto1.fetchall())
print("")

query_produto100 = cursor.execute("""SELECT * FROM produto WHERE preco > 100;""")
print("Produtos maiores que R$100 ",query_produto100.fetchall())
print("")

query_produto500 = cursor.execute("""SELECT * FROM produto WHERE preco < 500;""")
print("Produtos menores que R$500  ",query_produto500.fetchall())
print("")

query_cidade = cursor.execute("""SELECT * FROM cliente WHERE cidade = 'Macapá';""")
print("Clientes de Macapá",query_cidade.fetchall())
print("")

query_estoque10 = cursor.execute("""SELECT * FROM produto WHERE estoque > 10;""")
print("Produtos com estoque maior que 10",query_estoque10.fetchall())
print("")

query_p100e5 = cursor.execute("""SELECT * FROM produto WHERE preco > 100 AND estoque > 5;""")
print("Produtos com preço maior que 100 e estoque maior que 5",query_p100e5.fetchall())
print("")

query_p50e20 = cursor.execute("""SELECT * FROM produto WHERE preco > 100 AND estoque > 5;""")
print("Produtos com preço menor que 50 e estoque maior que 20",query_p50e20.fetchall())
print("")

query_clientesA = cursor.execute("""SELECT * FROM cliente WHERE nome LIKE 'A%';""")
print("Clientes que o nome cpomeça com A",query_clientesA.fetchall())
print("")

query_produtonote = cursor.execute("""SELECT * FROM produto WHERE nome LIKE 'note%';""")
print("Produtos que começam com note",query_produtonote.fetchall())
print("")

query_produto100and500 = cursor.execute("""SELECT * FROM produto WHERE preco BETWEEN 100 AND 500;""")
print("Produtos que preço entre 100 a 500",query_produto100and500.fetchall())
print("")

query_precocrescente = cursor.execute("""SELECT * FROM produto ORDER BY preco ASC;""")
print("Produtos com preço crescente",query_precocrescente.fetchall())
print("")

query_precodecrescente = cursor.execute("""SELECT * FROM produto ORDER BY preco DESC;""")
print("Produtos com preço decrescente",query_precodecrescente.fetchall())
print("")

query_clientesordenado = cursor.execute("""SELECT * FROM cliente ORDER BY nome;""")
print("Clientes ordenados por nome",query_clientesordenado.fetchall())
print("")

query_produtopreconome = cursor.execute("""SELECT * FROM produto ORDER BY preco DESC, nome ASC;""")
print("Produtos ordenados por preço decrescente, nome crescente",query_produtopreconome.fetchall())
print("")

conn.close()