# Smart Sort: QR-Based Waste Segregation & Recycling Awareness

Hack for Social Cause - Team **Arcvis Qelos** (HSC|TN|03295), Tamil Nadu. Theme: Environment & Sustainability.

Colour-coded bins carry a QR code. Scanning it opens a Tamil/English guide for that bin and lets anyone report overflow or wrong waste. Staff get a dashboard to resolve reports and log collected weight.

**SDGs:** 11 (Sustainable Cities), 12 (Responsible Consumption), 13 (Climate Action).

## Features
- Bilingual (Tamil/English) sorting guide per bin, mobile-first, no external CDN
- Report form: full, wrong waste, damaged label, or fine
- Staff dashboard: open reports, counts by type, weight by category, mark resolved
- QR generator for printing labels
- Sample data and automated tests

## Setup
Requires Python 3.10+.
```bash
git clone <your-repo-url> && cd smart-sort-campus-waste
python -m venv venv && source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                # then edit values
export $(grep -v '^#' .env | xargs)                 # Windows: set each variable manually
python app.py
```
Open http://localhost:5000. The database is created with sample data on first run.

### Environment variables
| Variable | Purpose | Default |
|---|---|---|
| `SECRET_KEY` | Signs session cookies. Use a long random value. | dev-only value |
| `DATABASE_URL` | SQLite file path | `smartsort.db` |
| `ADMIN_PASSWORD` | Staff dashboard password | `admin` (change it) |
| `BASE_URL` | Address encoded in QR codes (your server URL) | `http://localhost:5000` |

### Generate QR codes
```bash
BASE_URL=https://your-server python scripts/generate_qr.py   # PNGs in qr_codes/
```

### Run tests
```bash
pytest -v
```

## Demo walkthrough
1. Open `/bin/LIB-WET-01?lang=ta` (the URL a QR code opens) and read the guide.
2. Submit a report from the form at the bottom.
3. Go to `/login`, sign in, and see the report on `/dashboard`; log a weight and mark the report resolved.

## Project layout
See [docs/TECHNICAL_DESIGN.md](docs/TECHNICAL_DESIGN.md) for the architecture diagram, data model and flows.

## Pilot plan
Audit waste points -> design labels -> deploy QR-linked app -> pilot one building -> collect reports weekly -> improve.

## Notes
- Sorting lists are a starting point. Check them against the Solid Waste Management Rules, 2016 and your local municipal practice before printing.
- Add real campus bins to `data/sample_data.sql` (or insert into the `bins` table) before the pilot.

## AI tool usage
Parts of this project (code scaffolding, wording, Tamil text drafts) were produced with AI assistance and reviewed by the team. Have a Tamil speaker review the Tamil text before printing labels.

## License
MIT - see [LICENSE](LICENSE).
