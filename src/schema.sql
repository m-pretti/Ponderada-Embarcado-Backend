/* Definindo a tabela leituras conforme o requisito 6.1 */
CREATE TABLE IF NOT EXISTS leituras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,        -- Identificador único [cite: 105, 106]
    temperatura REAL NOT NULL,                   -- Valor da temperatura [cite: 107, 108]
    umidade REAL NOT NULL,                       -- Valor da umidade [cite: 109, 110]
    pressao REAL,                                -- Pressão (opcional) [cite: 111, 112]
    localizacao TEXT DEFAULT 'Lab',              -- Localização (opcional) [cite: 114, 115]
    timestamp DATETIME DEFAULT (datetime('now', 'localtime')) -- Data/Hora automática [cite: 117]
);