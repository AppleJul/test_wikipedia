# Test cases

site: en.wikipedia.org

---

## #1 Log in

#### Preconditions

Unauthenticated user

#### Steps

1) Open main page
2) Click login
3) Input test user and password
4) Click Log in

#### Expected result

- Redirection to main page
- Username in the user menu

---

## #2 Search

#### Preconditions

Unauthenticated user

#### Steps

1) Open main page
2) Click search input field
3) Type "Bernau"
4) Click "Bernau bei Berlin"

#### Expected result

- Redirection to article page "Bernau bei Berlin"

---

## #3 Random article

#### Preconditions

Unauthenticated user

#### Steps

1) Open main page
2) Open Side menu
3) Click "Random article"

#### Expected result

- Redirection to random article page

---

## #4 Open Article from news

#### Preconditions

Unauthenticated user

#### Steps

1) Open main page
2) Scroll to news
3) Click first highlighted article link

#### Expected result

- Redirection to article page

---

## #5 Watch List

#### Preconditions

Authenticated user

#### Steps

1) Open page Special:Watchlist
2) Check "You have [X] page(s) on your watchlist"
3) Open random article page
4) Click add to watchlist (starring button)
5) Open page Special:Watchlist


#### Expected result

You have [X+1] page(s) on your watchlist

---