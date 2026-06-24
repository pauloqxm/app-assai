# Deploy no Railway — Proximidades do Assaí

## Estrutura do projeto

```
app_assai/
├── Dockerfile          # Build de produção (Railway usa automaticamente)
├── requirements.txt    # Sem dependências externas (stdlib)
├── server.py           # Servidor HTTP estático
├── index.html          # Frontend (MapLibre GL)
├── dados/              # GeoJSON (obrigatório no deploy)
│   ├── assai.geojson
│   ├── Goiania.geojson
│   ├── setores.geojson
│   └── mercantis.geojson
└── DEPLOY.md
```

## Pré-requisitos

- Conta no [GitHub](https://github.com)
- Conta no [Railway](https://railway.app)
- Git instalado

## Passo 1: Repositório GitHub

```bash
cd "g:\Meu Drive\1. NUVEM\DADOS\Sites\app_assai"

git init
git add Dockerfile requirements.txt server.py index.html dados/
git commit -m "Deploy: Proximidades do Assaí"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/app-assai.git
git push -u origin main
```

> **Importante:** confirme que a pasta `dados/` foi commitada (os GeoJSON são servidos em `/dados/*.geojson`).

## Passo 2: Deploy no Railway

### Opção A — Dashboard (recomendado)

1. Acesse https://railway.app e faça login com GitHub
2. **New Project** → **Deploy from GitHub repo**
3. Selecione o repositório `app-assai`
4. Railway detecta o `Dockerfile` e faz o build automaticamente
5. Em **Settings** → **Networking** → **Generate Domain**
6. Acesse o domínio gerado (ex.: `https://app-assai.up.railway.app`)

### Opção B — Railway CLI

```bash
npm i -g @railway/cli
railway login
railway init
railway up
```

## Passo 3: Verificar

Após o deploy, teste:

| URL | Esperado |
|-----|----------|
| `/` | Página do mapa |
| `/dados/setores.geojson` | GeoJSON dos setores |
| `/dados/mercantis.geojson` | GeoJSON dos mercantis |

## Variáveis de ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `PORT` | `8000` | Definida automaticamente pelo Railway |
| `HOST` | `0.0.0.0` | Interface de escuta (não alterar em produção) |

Não é necessário configurar variáveis manualmente para o deploy básico.

## Build local (opcional)

```bash
docker build -t app-assai .
docker run -p 8000:8000 -e PORT=8000 app-assai
# http://localhost:8000
```

## Atualizações automáticas

Qualquer `git push` na branch conectada dispara novo deploy no Railway.

## Troubleshooting

### Página carrega mas mapa sem dados
- Verifique se `dados/` está no repositório (`git ls-files dados/`)
- Abra DevTools → Network e confira se `/dados/*.geojson` retorna 200

### Build failed
- Confira logs no Railway Dashboard → Deployments
- Teste localmente: `docker build -t app-assai .`

### Port already in use / app não inicia
- O `server.py` lê `PORT` do ambiente — não fixe porta no código

### Rota OSRM não funciona em produção
- A API OSRM (`router.project-osrm.org`) é externa; requer HTTPS e conexão de saída (Railway permite por padrão)

## Monitoramento

No Railway Dashboard:
- **Deployments** — histórico e rollback
- **Logs** — requisições e erros em tempo real
- **Metrics** — CPU e memória
