# Mesa

A small phone app for your favourite restaurants in Madrid, the Costa Brava and Vienna. The list lives in Notion
(**Restaurant Favourites**); Mesa shows it, helps you book, and records what you learn (whether a card was needed,
when you last went).

## What it does

- **Places:** filter by city, search, favourites, "Ready to book". Each place shows how you book it and whether it needs a card.
- **Book a table:** pick date, time and party size. Mesa writes the message for you (Spanish for Madrid and the Costa Brava, German for Vienna),
  opens the restaurant's own booking page, WhatsApp or the phone.
- **I booked it:** saves the table to your Google Calendar as "🍽 Name", then asks once whether a card was needed and stores the answer in Notion.
- **Wishlist (🔖 To try):** places you have not been to yet live in the same Notion database, marked "Not been yet" (dashed card). Add one with +
  (it starts as "Not yet" when the 🔖 filter is on), note why or who recommended it, and tap **I've been here** to turn it into a normal place
  (visit count and date are set; star it if it is a favourite). **Remove from list** archives it in Notion, with Undo.
- **Share ↗:** pick some places (or ★ favourites, or everywhere you've been), choose English, Spanish or German, and send a ready-made list with
  website and map links through WhatsApp or the phone's share sheet. Places you have not been to are only included if you tick them.
- **Bookings:** upcoming tables, and "Did you go?" afterwards, which updates last visit and visit count in Notion.

## What it does not do

Mesa does not book by itself and never handles card numbers. Most of these sites use a captcha and bank card checks, and some forbid automation.
When a restaurant wants a card, use a one-time Revolut card on the restaurant's own page.

## Setup

1. **Notion:** *Restaurant Favourites* needs two columns, **Wishlist** (select: Want to try, Booked) and **Why / recommended by** (text); both were added on 2026-11-04. Open *Restaurant Favourites*, then ••• > Connections, and add the same integration My Day uses.
2. **Worker:** from `Calorie tracker/worker`, run `npx wrangler deploy` (it already has `NOTION_RESTAURANTS_DB`).
   Add this app's address to `ALLOWED_ORIGIN` in `wrangler.toml` first (origin only, e.g. `https://mydayappmh.github.io`).
3. **App:** publish this folder on GitHub Pages, open it on your phone, go to Settings, and enter the same Worker address and app key as My Day.
   "Check connection" shows what is missing.
4. Add to home screen.

Icons: `python3 scripts/make-icons.py` (needs Pillow).

## Add a place from Google Maps

In Google Maps, open a place, tap Share and pick Mesa. It lands in 🔖 To try with its name and address, and nothing is added twice.
- **Android:** install Mesa to the home screen first (Chrome, ⋮, Install app). Mesa then shows up in the share sheet.
- **iPhone:** iOS cannot share straight into a web app, so use a Shortcut that sends the shared text to the Worker (`POST /api/restaurants/share` with the `X-App-Key` header and `{"text": …}` as JSON).
