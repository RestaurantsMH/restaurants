# Mesa

A small phone app for your favourite restaurants in Madrid, the Costa Brava and Vienna. The list lives in Notion
(**Restaurant Favourites**); Mesa shows it, helps you book, and records what you learn (whether a card was needed,
when you last went).

## What it does

- **Places:** filter by city, search, favourites, "Ready to book". Each place shows how you book it and whether it needs a card.
- **Book a table:** pick date, time and party size. Mesa writes the message for you (Spanish for Madrid and the Costa Brava, German for Vienna),
  opens the restaurant's own booking page, WhatsApp or the phone.
- **I booked it:** saves the table to your Google Calendar as "🍽 Name", then asks once whether a card was needed and stores the answer in Notion.
- **Bookings:** upcoming tables, and "Did you go?" afterwards, which updates last visit and visit count in Notion.

## What it does not do

Mesa does not book by itself and never handles card numbers. Most of these sites use a captcha and bank card checks, and some forbid automation.
When a restaurant wants a card, use a one-time Revolut card on the restaurant's own page.

## Setup

1. **Notion:** open *Restaurant Favourites*, then ••• > Connections, and add the same integration My Day uses.
2. **Worker:** from `Calorie tracker/worker`, run `npx wrangler deploy` (it already has `NOTION_RESTAURANTS_DB`).
   Add this app's address to `ALLOWED_ORIGIN` in `wrangler.toml` first (origin only, e.g. `https://mydayappmh.github.io`).
3. **App:** publish this folder on GitHub Pages, open it on your phone, go to Settings, and enter the same Worker address and app key as My Day.
   "Check connection" shows what is missing.
4. Add to home screen.

Icons: `python3 scripts/make-icons.py` (needs Pillow).
