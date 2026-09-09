# Soul Hunter - Backend

API de captura de fantasmas. Backend em Flask + psycopg (PostgreSQL/Neon), sem ORM.

## Como rodar

1. **Criar ambiente virtual** (uma vez):
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate        # Windows
   source .venv/bin/activate       # Linux/Mac
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar `.env`** com a conexao do Neon:
   ```
   DATABASE_URL=postgresql://...
   CORS_ORIGINS=http://localhost:3000
   ```

4. **Popular dados de demonstracao** (casa + fantasmas + spawns):
   ```bash
   python seed.py
   ```

5. **Subir o servidor**:
   ```bash
   python app.py
   ```

## Rotas

| Metodo | Rota                 | Descricao                                   |
|--------|----------------------|---------------------------------------------|
| GET    | `/`                  | Informacao da API                           |
| GET    | `/health`            | Status do servidor e do banco               |
| POST   | `/usuario`           | Criar usuario `{nome, email, senha}`        |
| GET    | `/usuario/<id>`      | Consultar usuario                            |
| POST   | `/casa/investigar`   | Sortear um fantasma na casa assombrada      |
| GET    | `/spawn`             | Pontos de spawn com fantasmas (mapa)        |
| POST   | `/captura`           | Capturar `{id_usuario, id_fantasma, latitude, longitude}` |
| GET    | `/fantasma/<id>`     | Consultar fantasma                           |

## Regras do jogo

- Raridade: COMUM (560/1000), RARO (350/1000), EPICO (75/1000), LENDARIO (15/1000).
- Pontos por captura: COMUM 10, RARO 25, EPICO 50, LENDARIO 100.
- Nivel: 1 nivel por 100 pontos acumulados.
- Captura so vale dentro do raio da casa (calculado por haversine).

## Testes

```bash
python -m pytest
```