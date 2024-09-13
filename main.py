from bs4 import BeautifulSoup

html='''
<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'none'; img-src data: *; object-src 'none'"></meta>
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks Menu</H1>

<DL><p>
    <DT><H3 ADD_DATE="1724244313" LAST_MODIFIED="1725972321">Mozilla Firefox</H3>
    <DL><p>
        <DT><A HREF="https://support.mozilla.org/kb/customize-firefox-controls-buttons-and-toolbars?utm_source=firefox-browser&utm_medium=default-bookmarks&utm_campaign=customize" ADD_DATE="1724244313" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://support.mozilla.org/kb/customize-firefox-controls-buttons-and-toolbars?utm_source=firefox-browser&utm_medium=default-bookmarks&utm_campaign=customize" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAHY0lEQVR4Aa3VA5RrSdfG8f+uOidJp/umczm2ffFhbNvG9722bdv22LZt+3I81+04B1XvfpPmWHut3yk06smus1Z4L8uXDv6MHzpowA8eWFS8FaY9eU+cCvxaFfF8W/FWGDy8a6n7DM7/H96DR3ldu0MVb8a0J+9CI1qXJP11a+79GOdP1f11FW/EtCfvQpx8mziFxMHEEEV1KYkrKl6Pea1Nbnrs/7hz7q2KUQsqRcUE/eV1acb/pyFQ7b9N3fguzNTxVsXrMa/avFgPb6SnukY8W6EgXvszrszjivH08F0VLZFK0rbUgRt9H2aS+lORznUxnTMV45kJG6fNPZSGnEodTJwUFGbphqdSll/H/SxWjEc92kYxSoO0uzEcwo90g/9rlKpHpCmX491MxQgzuvjtE0UieyqxhYZA3UGp8CjUtSMR2YrkFdf+/szi9X88+zM3/uncSx/81/f+7/HzPsu8q09i8MUNcCUHUTImceAAL+RC+UW1nMzHuUvxSVGBCloTgMT+GuOLipaGyg/OpLuE/jVI58wHb/zsdxD5tBVbDMQwOPe/8UDqHYuuPJjCZnP5nw/+mfyUPhADRtkAaIfosum23klBxH8b+KzCfuczG8IPXi4C5yHQwvDoPYhCBSkz1n9y1+WLd8xFzVUxxmIRjBIBVHXFZF58aEtW3exxsp0V8Aac8gpBnGQBRNymkP4VXKPdgdj8H2JB/DgMVwreATFhdoCdj/wY8x7+GM8/djyJ81hlnCPTUWfHb/0QlyRUelalEPcCHswIQARJPd64ohh/KHBagPcQB7sggHgIVHcM0wUyWWUAoNaEuobI9bP1dj9lw1nnMvehj/LS0wdinYO4wM1f/h6z3v9n1t3pTnAWBj04ZQA7LFROwMsu7QCpgcjuCh4Asg5Wa0ImgNDqqHTOtDyIgPPKkZ/cZOstzmT+Nw4jcA5JBO9SHjzzWKZt8CRd03ohD/RZALCigIwHawBmKgKSVoAiAi2VDCzsgo0bYB04lSojEAaQDyETsmTZf3PPdZ+irvMgTTF4SAVX7+SRC/dj5/f/C6D9d5UQLBAIFBJILIhtB1g2a8uZq+1+LwiAV8CSTujPwqoRbJjCJMdAeRVue+j/WLh4T2I3jcCEhN4ShmDFYR2IAXC8OHdDaMYAYBxU82AFAgPShHoejAEgUEViy2h5UbS9LLBajf5oMr866wc0wlWQvEEyNQKbIcSSwZBNIfAO41NQ9ZXd0IgBAQdUDAQWpjQhcfi6gCgguDtTm3vIUBdhdwUA/Pggqmy49/n/pr/q8ZMq4DziEwI0QOtpiT1kXUqQRqC8ohaDy0BqoGzxOUE6q9DwMBiOvtzm5OLi3migAFEwpjnOCzmKhZXUkyr1uEwtLqky1aStNk4jqhFFDVZb6ykYMjBodQxw5RAKZUgSqAq+YmmWzFxF0P8L61Z8pHhf5/S+bfHQJm1OLcuzw4YPcWH3/qysTcebFHyESTOkhLjUokt8M8VFCVYDbLXhvdCfARfiG3lkykDr2qhbXJTRUZBAngMwootGI3tbrbcIsR3ugp3Yhbun89l9/ko+qCDVGpQruHKJqDakBmnq2KyXaDZKrDX1KWau+ij0ZqAvgwR1JFuFmihwPTkdDQN9co3C6IMnwujs0sppELcOV+NHVc2wzv2eb+74J6ZP6kGazeEgZZJqiaRWJo6qbDb5MU7c4ixYmYUhC7YJaQxVgYrgSxa3sgNftdww31+usFuvuykfWDzU/4HytL0llTVz+SbiAScTryKxFFc6dlnnQVZP+wEo2grT7ACb5V7g2BnXsVfxHsLEgfGQTYb/1kJqWpKV3VDLM1iXi/a8PDrtqmecl451DwLg8oG1DtnMmcsKq/bQ1V3BmBTsfzgIfHucwINxICivADt8eADkBLJGtcc0ydHsmU7QEXBFfzwTeFwRnLFtDoBD7nv5+vv61v2XXzHlfR7oKtQxLkFcCqkDK8qMHdIex4gSMxaoKZBtS8lQ18NtJsPSmv/Nyfc3nma4RjsA8Jnq1HU+WC9cY01z865pJQrdDcQkrW6IpGOfun3oxLnw6m/SEBIyVFbOIMhmiXJy35oL+vYDBhkuGxY3YaTuy9TLA+Jv2inu2j2ph9NrTUMmCyIGjwEnyiCtUaUWnGlLR1hIlM6rKwpUX5qBiTuI02Du94aqx8zJhEsVI4IPduUZV+7vDC0CDv9GdeolUjObL18ckutqMKkQkc2kiFHOITLCwyiUp1bNUhuYRFrrxPoMzdDM/XbUf/gZvvYsozX+Cl5d5vh690afrk3+0hR4XyoxqYmQICaTSwjClI6cA3EIvhWi0QiIm6rRgaQh1ikfsMK43/xv8YWfASuUe6sBAIzqPmNwjb1nJdnP5PDbOpPgJMXjWhDAC4JgvEWUaQkoib/o/NzQb37S1fP0+Dt/6wHGKqe6v1yZvuG+zc69p3m7d4dnW8TjAaEdwmFKEcztkfSG67KVG346aeV8YEglincRYLQClVcdKsery6lI1VVNJbyF+jdp8gPG4E08mAAAAABJRU5ErkJggg==">Customize Firefox</A>
        <DT><A HREF="https://www.mozilla.org/contribute/" ADD_DATE="1724244313" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.mozilla.org/contribute/" ICON="data:image/png;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxNicgaGVpZ2h0PScxNic+IDxwYXRoIGQ9J00wIDBoMTZ2MTZIMHonLz4gPHBhdGggZD0nTTEzLjk5NCAxMC4zNTZIMTVWMTJoLTMuMTcxVjcuNzQxYzAtMS4zMDgtLjQzNS0xLjgxLTEuMjktMS44MS0xLjA0IDAtMS40Ni43MzctMS40NiAxLjh2Mi42M2gxLjAwNlYxMkg2LjkxOFY3Ljc0MWMwLTEuMzA4LS40MzUtMS44MS0xLjI5MS0xLjgxLTEuMDM5IDAtMS40NTkuNzM3LTEuNDU5IDEuOHYyLjYzaDEuNDQxVjEySDF2LTEuNjQ0aDEuMDA2VjYuMDc5SDFWNC40MzVoMy4xNjh2MS4xMzlhMi41MDcgMi41MDcgMCAwIDEgMi4zLTEuMjlBMi40NTIgMi40NTIgMCAwIDEgOC45MzEgNS45MSAyLjUzNSAyLjUzNSAwIDAgMSAxMS40IDQuMjg0IDIuNDQ4IDIuNDQ4IDAgMCAxIDE0IDYuOXYzLjQ1OHonIGZpbGw9JyNmZmYnLz4gPC9zdmc+">Get Involved</A>
        <DT><A HREF="https://www.mozilla.org/about/" ADD_DATE="1724244313" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.mozilla.org/about/" ICON="data:image/png;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxNicgaGVpZ2h0PScxNic+IDxwYXRoIGQ9J00wIDBoMTZ2MTZIMHonLz4gPHBhdGggZD0nTTEzLjk5NCAxMC4zNTZIMTVWMTJoLTMuMTcxVjcuNzQxYzAtMS4zMDgtLjQzNS0xLjgxLTEuMjktMS44MS0xLjA0IDAtMS40Ni43MzctMS40NiAxLjh2Mi42M2gxLjAwNlYxMkg2LjkxOFY3Ljc0MWMwLTEuMzA4LS40MzUtMS44MS0xLjI5MS0xLjgxLTEuMDM5IDAtMS40NTkuNzM3LTEuNDU5IDEuOHYyLjYzaDEuNDQxVjEySDF2LTEuNjQ0aDEuMDA2VjYuMDc5SDFWNC40MzVoMy4xNjh2MS4xMzlhMi41MDcgMi41MDcgMCAwIDEgMi4zLTEuMjlBMi40NTIgMi40NTIgMCAwIDEgOC45MzEgNS45MSAyLjUzNSAyLjUzNSAwIDAgMSAxMS40IDQuMjg0IDIuNDQ4IDIuNDQ4IDAgMCAxIDE0IDYuOXYzLjQ1OHonIGZpbGw9JyNmZmYnLz4gPC9zdmc+">About Us</A>
        <DT><A HREF="https://support.mozilla.org/products/firefox" ADD_DATE="1676142694" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://support.mozilla.org/products/firefox" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAHY0lEQVR4Aa3VA5RrSdfG8f+uOidJp/umczm2ffFhbNvG9722bdv22LZt+3I81+04B1XvfpPmWHut3yk06smus1Z4L8uXDv6MHzpowA8eWFS8FaY9eU+cCvxaFfF8W/FWGDy8a6n7DM7/H96DR3ldu0MVb8a0J+9CI1qXJP11a+79GOdP1f11FW/EtCfvQpx8mziFxMHEEEV1KYkrKl6Pea1Nbnrs/7hz7q2KUQsqRcUE/eV1acb/pyFQ7b9N3fguzNTxVsXrMa/avFgPb6SnukY8W6EgXvszrszjivH08F0VLZFK0rbUgRt9H2aS+lORznUxnTMV45kJG6fNPZSGnEodTJwUFGbphqdSll/H/SxWjEc92kYxSoO0uzEcwo90g/9rlKpHpCmX491MxQgzuvjtE0UieyqxhYZA3UGp8CjUtSMR2YrkFdf+/szi9X88+zM3/uncSx/81/f+7/HzPsu8q09i8MUNcCUHUTImceAAL+RC+UW1nMzHuUvxSVGBCloTgMT+GuOLipaGyg/OpLuE/jVI58wHb/zsdxD5tBVbDMQwOPe/8UDqHYuuPJjCZnP5nw/+mfyUPhADRtkAaIfosum23klBxH8b+KzCfuczG8IPXi4C5yHQwvDoPYhCBSkz1n9y1+WLd8xFzVUxxmIRjBIBVHXFZF58aEtW3exxsp0V8Aac8gpBnGQBRNymkP4VXKPdgdj8H2JB/DgMVwreATFhdoCdj/wY8x7+GM8/djyJ81hlnCPTUWfHb/0QlyRUelalEPcCHswIQARJPd64ohh/KHBagPcQB7sggHgIVHcM0wUyWWUAoNaEuobI9bP1dj9lw1nnMvehj/LS0wdinYO4wM1f/h6z3v9n1t3pTnAWBj04ZQA7LFROwMsu7QCpgcjuCh4Asg5Wa0ImgNDqqHTOtDyIgPPKkZ/cZOstzmT+Nw4jcA5JBO9SHjzzWKZt8CRd03ohD/RZALCigIwHawBmKgKSVoAiAi2VDCzsgo0bYB04lSojEAaQDyETsmTZf3PPdZ+irvMgTTF4SAVX7+SRC/dj5/f/C6D9d5UQLBAIFBJILIhtB1g2a8uZq+1+LwiAV8CSTujPwqoRbJjCJMdAeRVue+j/WLh4T2I3jcCEhN4ShmDFYR2IAXC8OHdDaMYAYBxU82AFAgPShHoejAEgUEViy2h5UbS9LLBajf5oMr866wc0wlWQvEEyNQKbIcSSwZBNIfAO41NQ9ZXd0IgBAQdUDAQWpjQhcfi6gCgguDtTm3vIUBdhdwUA/Pggqmy49/n/pr/q8ZMq4DziEwI0QOtpiT1kXUqQRqC8ohaDy0BqoGzxOUE6q9DwMBiOvtzm5OLi3migAFEwpjnOCzmKhZXUkyr1uEwtLqky1aStNk4jqhFFDVZb6ykYMjBodQxw5RAKZUgSqAq+YmmWzFxF0P8L61Z8pHhf5/S+bfHQJm1OLcuzw4YPcWH3/qysTcebFHyESTOkhLjUokt8M8VFCVYDbLXhvdCfARfiG3lkykDr2qhbXJTRUZBAngMwootGI3tbrbcIsR3ugp3Yhbun89l9/ko+qCDVGpQruHKJqDakBmnq2KyXaDZKrDX1KWau+ij0ZqAvgwR1JFuFmihwPTkdDQN9co3C6IMnwujs0sppELcOV+NHVc2wzv2eb+74J6ZP6kGazeEgZZJqiaRWJo6qbDb5MU7c4ixYmYUhC7YJaQxVgYrgSxa3sgNftdww31+usFuvuykfWDzU/4HytL0llTVz+SbiAScTryKxFFc6dlnnQVZP+wEo2grT7ACb5V7g2BnXsVfxHsLEgfGQTYb/1kJqWpKV3VDLM1iXi/a8PDrtqmecl451DwLg8oG1DtnMmcsKq/bQ1V3BmBTsfzgIfHucwINxICivADt8eADkBLJGtcc0ydHsmU7QEXBFfzwTeFwRnLFtDoBD7nv5+vv61v2XXzHlfR7oKtQxLkFcCqkDK8qMHdIex4gSMxaoKZBtS8lQ18NtJsPSmv/Nyfc3nma4RjsA8Jnq1HU+WC9cY01z865pJQrdDcQkrW6IpGOfun3oxLnw6m/SEBIyVFbOIMhmiXJy35oL+vYDBhkuGxY3YaTuy9TLA+Jv2inu2j2ph9NrTUMmCyIGjwEnyiCtUaUWnGlLR1hIlM6rKwpUX5qBiTuI02Du94aqx8zJhEsVI4IPduUZV+7vDC0CDv9GdeolUjObL18ckutqMKkQkc2kiFHOITLCwyiUp1bNUhuYRFrrxPoMzdDM/XbUf/gZvvYsozX+Cl5d5vh690afrk3+0hR4XyoxqYmQICaTSwjClI6cA3EIvhWi0QiIm6rRgaQh1ikfsMK43/xv8YWfASuUe6sBAIzqPmNwjb1nJdnP5PDbOpPgJMXjWhDAC4JgvEWUaQkoib/o/NzQb37S1fP0+Dt/6wHGKqe6v1yZvuG+zc69p3m7d4dnW8TjAaEdwmFKEcztkfSG67KVG346aeV8YEglincRYLQClVcdKsery6lI1VVNJbyF+jdp8gPG4E08mAAAAABJRU5ErkJggg==">Obtener ayuda</A>
        <DT><A HREF="https://support.mozilla.org/kb/customize-firefox-controls-buttons-and-toolbars?utm_source=firefox-browser&utm_medium=default-bookmarks&utm_campaign=customize" ADD_DATE="1676142694" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://support.mozilla.org/kb/customize-firefox-controls-buttons-and-toolbars?utm_source=firefox-browser&utm_medium=default-bookmarks&utm_campaign=customize" ICON="data:image/png;base64,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">Personalice Firefox</A>
        <DT><A HREF="https://www.mozilla.org/contribute/" ADD_DATE="1676142694" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.mozilla.org/contribute/" ICON="data:image/png;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxNicgaGVpZ2h0PScxNic+IDxwYXRoIGQ9J00wIDBoMTZ2MTZIMHonLz4gPHBhdGggZD0nTTEzLjk5NCAxMC4zNTZIMTVWMTJoLTMuMTcxVjcuNzQxYzAtMS4zMDgtLjQzNS0xLjgxLTEuMjktMS44MS0xLjA0IDAtMS40Ni43MzctMS40NiAxLjh2Mi42M2gxLjAwNlYxMkg2LjkxOFY3Ljc0MWMwLTEuMzA4LS40MzUtMS44MS0xLjI5MS0xLjgxLTEuMDM5IDAtMS40NTkuNzM3LTEuNDU5IDEuOHYyLjYzaDEuNDQxVjEySDF2LTEuNjQ0aDEuMDA2VjYuMDc5SDFWNC40MzVoMy4xNjh2MS4xMzlhMi41MDcgMi41MDcgMCAwIDEgMi4zLTEuMjlBMi40NTIgMi40NTIgMCAwIDEgOC45MzEgNS45MSAyLjUzNSAyLjUzNSAwIDAgMSAxMS40IDQuMjg0IDIuNDQ4IDIuNDQ4IDAgMCAxIDE0IDYuOXYzLjQ1OHonIGZpbGw9JyNmZmYnLz4gPC9zdmc+">Involúcrese</A>
        <DT><A HREF="https://www.mozilla.org/about/" ADD_DATE="1676142694" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.mozilla.org/about/" ICON="data:image/png;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxNicgaGVpZ2h0PScxNic+IDxwYXRoIGQ9J00wIDBoMTZ2MTZIMHonLz4gPHBhdGggZD0nTTEzLjk5NCAxMC4zNTZIMTVWMTJoLTMuMTcxVjcuNzQxYzAtMS4zMDgtLjQzNS0xLjgxLTEuMjktMS44MS0xLjA0IDAtMS40Ni43MzctMS40NiAxLjh2Mi42M2gxLjAwNlYxMkg2LjkxOFY3Ljc0MWMwLTEuMzA4LS40MzUtMS44MS0xLjI5MS0xLjgxLTEuMDM5IDAtMS40NTkuNzM3LTEuNDU5IDEuOHYyLjYzaDEuNDQxVjEySDF2LTEuNjQ0aDEuMDA2VjYuMDc5SDFWNC40MzVoMy4xNjh2MS4xMzlhMi41MDcgMi41MDcgMCAwIDEgMi4zLTEuMjlBMi40NTIgMi40NTIgMCAwIDEgOC45MzEgNS45MSAyLjUzNSAyLjUzNSAwIDAgMSAxMS40IDQuMjg0IDIuNDQ4IDIuNDQ4IDAgMCAxIDE0IDYuOXYzLjQ1OHonIGZpbGw9JyNmZmYnLz4gPC9zdmc+">Acerca de nosotros</A>
        <DT><H3 ADD_DATE="1654974294" LAST_MODIFIED="1724671971">TV</H3>
        <DL><p>
            <DT><A HREF="https://orangetv.orange.es/brw" ADD_DATE="1626710512" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://orangetv.orange.es/brw" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAc0lEQVQ4jWP8X8lAEmAiTfmohsGigQVK/ydCLSNcAyMTg0kig4Q+w/+/OJQyM7y4yHB2PsP/fzANmr4Mmv74jL++keHcQpiG//8ZHp9iYGTGZ8PjUwz//zMwMDBCUysjMwMjIz4b/v+HGAf39F+i/M3AAAB83CJUD5vU4QAAAABJRU5ErkJggg==">Orange</A>
            <DT><A HREF="https://www.youtube.com/" ADD_DATE="1665723676" LAST_MODIFIED="1724671971" ICON_URI="https://www.youtube.com/s/desktop/4151fd0f/img/favicon.ico" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAtklEQVQ4T2NkoBAwUqifAW7AfwYGAaBhBlADHXAYfAAqfgGo8QOIDTYAqDkBSM0n0TWJQM0LGIGaQbaeJ1EzTLkhyIAAIG89mQYkggxoAGqux2rAgwdAzwF9dwDmdQxVjfgN+A80HgQ2bmRgKChgYAAZiAqINODgQYhLSDYApAFk84YNuIII7ALcgSgATBofwNGNC4ADkbJoBBlNUUKCuQ0tKYNcBUra6AAWn6hJGZ8nCclRnBsBzJ03KZWC+NsAAAAASUVORK5CYII=">(61) YouTube</A>
            <DT><A HREF="https://www.netflix.com/es/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse" ADD_DATE="1596311444" LAST_MODIFIED="1724671971">Netflix</A>
            <DT><A HREF="https://www.netflix.com/es-en/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse" ADD_DATE="1596311444" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.netflix.com/es-en/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABtklEQVQ4jX2SO09UURSFv7XPvRcZHoMYSSQ2lsbS3lYSW/05xv/jo1MDMbGx9tGQ2BgSCzABFUHQO8zdy2IwmRlxVreL/Z1v5ywAHkMB+FgtP/zerHq3uewvzer2DlwCeF2tPH9Z9/2q7nurWn40vhOM5XOmWkHiQYVv9qr+HQA7A5uLEgBPzodjUt8yqRxdjVQp7gMgsPR/wIPzYS7C+zadHL+wz0L3vsJy2q1mGfxNneiI5NCOhG7OrHdl8e4xPilwIWECUEUAYs8dBRzCTak2Du0usWzIWYAhyZxgL63fUE5tBtLG0Lp9AhmaWpgGJEENnNrezwRwmvUV6dax3RU822AU0YTYydGDhrwRkS0efccsQAAdZkkqh+ntELsYrUUwb+kME1MOUydAWiyiKOG3TWqzJzEP3brCrU1MSf9jII1605fKIAebKdSBrkVgC3KGgUhj0yEtooXS/dxqYVdQVqRcErQx2YcJQEcIyZazkporcFSnX8yDKzNcU7jNFGP1nwAU0rJVWyHTAAydT40iRe9qhBYIM1b/KQMyzUHB7xvrA8Cn4Y83hmc9eFfjg+sREyf8AWnA2hnevZkcAAAAAElFTkSuQmCC">Netflix</A>
            <DT><A HREF="https://pluto.tv/?utm_source=google&utm_medium=textsearch&utm_campaign=1000710&utm_content=10000162&gclid=Cj0KCQjw37iTBhCWARIsACBt1IxSbMUhfgR3zcpVN3I4eJAHu8DBWzBUoS6Pw7rZlD4Af_SVeVETQKsaAn-vEALw_wcB" ADD_DATE="1651452293" LAST_MODIFIED="1724671971">Pluto TV - Drop in. Watch Free.</A>
            <DT><A HREF="https://www.youtube.com/watch?v=GDy53TIdNnE" ADD_DATE="1652305521" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.youtube.com/watch?v=GDy53TIdNnE" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABx0lEQVQ4jZ2TQWtTQRDHfzO7yUsNKSG0heJJ0YKnCvVSkHrV7+BBeu7Vk9+lH8CLN6EXk4Lo1V48lGClFBELGmmSmr73djy8fS8vll4c+LO7s7OzM///LhQmBmrg+uDtZrgIBQQAKyf/YQbiBexFt9t9niSP7ji3umrW7og0UfWL0ZaOzGYjmBxn2c/BdPpJxuNz+vDwFxxnqmaqZs4V8L5AuS6haqmqXcDpO3jCEN4YmEFmkMcxrSCSGqSh8GcGIY52Am91Ce5HJ5EYBRwbG45222HmUHVS+DX2DhASuKu3oAeolGSqCiDs7gqHh8L2thCCxOQSbxFAO9BToClzNQSJokwmsLUFgwHs78P6eklnlQho6c0axUKbTVhZgUYjHpeqCwE8kMWFxYNF9uVlGA5hbw8ODuqJzajqnPENPtfYDxU2N4OtrRVzkVDfC0V8/h2G/g98AR7ESkJF8tFRcYdzkOf15iRW6y/hlD48voCz+BbmELFrvhrG8OMjPBOAV3D7qXM791R73Var00qSJRoNTyifB5Dn+eVsNv19dTX+mmWj93n+4SWciM1LKkmqy7RoImFBqPqPfH39K7t/4A18f74nAH8Bjm35s3ZkOjEAAAAASUVORK5CYII=">(350) Rockin’1000 - that’s live - Cesena - july 24th 2016 - YouTube</A>
            <DT><A HREF="https://www.twitch.tv/" ADD_DATE="1663546869" LAST_MODIFIED="1724671971" ICON_URI="https://assets.twitch.tv/assets/favicon-16-52e571ffea063af7a7f4.png" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACpSURBVHgB1ZHBDQIhEEX/GGvDNqxA3YNn2QrMagVGrxYgVmApe9QCdhQMEUdWIHvanwCTybzPDBAC7RVvOkAjU0tDNI3Bi0sa3s3e50TCpXIG/2B/k4y/DIZoBAbhj/j40RYYSFn4vHYPXxcbePjeoq4MaZsjuzWKOQbYlm+n1zp+ch2jqa60Qs4IPzBwCOG0gYQNzWUNxUA/Uh+U1YGbNQH3aqtY59Y+AYmPQ7sreL+6AAAAAElFTkSuQmCC">Twitch</A>
            <DT><A HREF="https://www.tiktok.com/@_aiitanaguerrero/video/7145808993078889733?is_copy_url=1&is_from_webapp=v1" ADD_DATE="1663798555" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.tiktok.com/@_aiitanaguerrero/video/7145808993078889733?is_copy_url=1&is_from_webapp=v1" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC6UlEQVQ4jU2TP2jcdRyGn/fz/d1dkrum5C7R9EwaKYJ/aPEvghQU2kUtKopDpqJ2MVMXLSouXcRN0EIpCsFJEWktNLroIIKbIi1FxMHSUmux5dL7kyZ39/u+DungO7zbAy8PvAKYmZnZ3VD9Q5GfD/IOgLBDYKeEQeScDWSiZ+LbvgfvdDqdy2o224t1xVrC+3CZw1bYgBGm6G/gCMZTdbIgS0YpSnRh4HwoNSenTyXpYORyGDiFMwGknImiUOeZ/dpo76J27RpJAhD2CEU7wS4ttNrdlPNUCEUulbADojIccrO50wf+OM9rvdCZ+57krK/m6WpDt4UzcqnYCNkNRMhZAYSRAhdJLnPWQ52uDt41zSvvHfVmltY9JmwJh+xG3NmEjAQopFq/r0rvlgqbzZQoBQfeXdEnF3/TE/sPEv2BSAmAkJC83ZGz6HV95dFHuPHcs5QJVEmk67e4/Pkay4t7+Kz5sPI4GyFhFUa2QM4aOXv94490ZGWFV4ew+uDTrDOCQY3jR95k6/gsezaqZseUGGeDKGxwCuJGh2vHjnJiZYXD5/+CUz9wdivRCUEEw5111v75nXoxSa2YwBhLFJIU2XSnJr335Rd0eDDm4kvHeP/Sd/w632KZAstEFjuqdTdSVZu2TciIyMhG3rK1ADZwmut8z4B/724RtQbqbzAux4xCGiNnSb7DRZYoi4Lq1shXv/oG1wuWvz7hB95+y/evnuT1qQaj0z/5Uu+mi6LisU1GtkSWYH5uqdueXRzvbi2Us41WPvnpaun/Z/VHfzD9uOdmZr2n1S4Xm7vyQuuest1aHM/PLXU1N7f0RUVaJueh8rgy2tzkxcee4tC9e/Gff+vcLz9zrtH1RFHFNpnAaERK1ZH9pZrN9mKlUlsLex/OOYF6gz4eDqFaEI0ppnOi9LZ1gx1FWFwYjbYOpdu3e91qtbmm5HnDkqE6OTFJrV6PieoE1SzGoO2PCit6FmdGo3ij07l85T8NMH/Iguw4NQAAAABJRU5ErkJggg==">TikTok - Make Your Day</A>
            <DT><A HREF="https://www.twitch.tv/elxokas" ADD_DATE="1663801773" LAST_MODIFIED="1724671971">elxokas - Twitch</A>
            <DT><A HREF="https://www.primevideo.com/" ADD_DATE="1667072861" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.primevideo.com/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACyUlEQVQ4jV2TPYidZRCFz5l35v3uL2RjEFJ4QbAwSsC4W0QWQ1Rs3CYgCBZCxKiFP2CTYBdBIlgIJli7hYKIWghJZSELGySVhVUKkZVVF8PusuSa+33vz6S4d0E93cwwMzDzHGIuAnAAOHr5+9MSm/NUPSOmE6qB0bYkhI0cfH3n1eWf/t1DHOry1/Foso/E9C32hw3goBA0BZsG0h+CXlqofrbd4H289Hh3OIV450Y8ovvfyvjImqeZ00KhqogpqQqqOlSrxBjC0gP02fT69rHei3jhkU4A+Lj78wpCs1YO9jrPyZGSSq1kLvCcUUshclZPycvunY690drxnXtXADoHr1xbCbHZhGkQFVJVaOZ3szP2IkbDHlwDPKiLKmFWJZqLWWlDXRXUcsHB6Ll1z4Wpzd4X5yfnnsDJB4f4e/8u0qyDlELPxZEzve3cqdE6XAh24vmPHX6M7gQgxZ2DqPjq9Wfw8qkJxjHg5+093Jm26FugA+TiaYQPpeY08bZl7fJiQ4KnjL1pi2FjuPTcY7j59rN4bXmC2awDS/FaMr2d0VOaqKe8IIBwASoFnvMhFnO5z3MpwzXM43nZFTltgeFRMLknF1CAnLE07GHaJlz94Rdc27iNnXsJS+MBatcRblWCgin9HvThp0960BWUUgiyOhBVGE3x3peb+OLmbTiBUWOoFQ4SICqtFzyn72hnL67A4ibNAoOQaiKm/k+qDL2I8agPDwGu5tRAmlZa42JaSFkN9bfNP+Shp5Zo/VXUlAAScOnF6BYEpTrcCcJJohLM0h9ZTbNPdz88tx4AsNqTP3Lgp2j9EygZAIpzgfnivgAKSWFvpD6bXt+f7byJWzdqAADs3ip1cPwb6Y2HIJapTWStdIAgSAqpUeC185KvHvz16xv4/FIHfAD+38529uJpWDxPDWeoNqEpRG0LFjbUZP1g/d3/2Pk+A7FTyqLANCwAAAAASUVORK5CYII=">Prime Video</A>
            <DT><A HREF="https://www.netflix.com/es/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Netflix</A>
            <DT><A HREF="https://orangetv.orange.es/brw" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://orangetv.orange.es/brw" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAc0lEQVQ4jWP8X8lAEmAiTfmohsGigQVK/ydCLSNcAyMTg0kig4Q+w/+/OJQyM7y4yHB2PsP/fzANmr4Mmv74jL++keHcQpiG//8ZHp9iYGTGZ8PjUwz//zMwMDBCUysjMwMjIz4b/v+HGAf39F+i/M3AAAB83CJUD5vU4QAAAABJRU5ErkJggg==">Orange</A>
            <DT><A HREF="https://www.netflix.com/es-en/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.netflix.com/es-en/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABtklEQVQ4jX2SO09UURSFv7XPvRcZHoMYSSQ2lsbS3lYSW/05xv/jo1MDMbGx9tGQ2BgSCzABFUHQO8zdy2IwmRlxVreL/Z1v5ywAHkMB+FgtP/zerHq3uewvzer2DlwCeF2tPH9Z9/2q7nurWn40vhOM5XOmWkHiQYVv9qr+HQA7A5uLEgBPzodjUt8yqRxdjVQp7gMgsPR/wIPzYS7C+zadHL+wz0L3vsJy2q1mGfxNneiI5NCOhG7OrHdl8e4xPilwIWECUEUAYs8dBRzCTak2Du0usWzIWYAhyZxgL63fUE5tBtLG0Lp9AhmaWpgGJEENnNrezwRwmvUV6dax3RU822AU0YTYydGDhrwRkS0efccsQAAdZkkqh+ntELsYrUUwb+kME1MOUydAWiyiKOG3TWqzJzEP3brCrU1MSf9jII1605fKIAebKdSBrkVgC3KGgUhj0yEtooXS/dxqYVdQVqRcErQx2YcJQEcIyZazkporcFSnX8yDKzNcU7jNFGP1nwAU0rJVWyHTAAydT40iRe9qhBYIM1b/KQMyzUHB7xvrA8Cn4Y83hmc9eFfjg+sREyf8AWnA2hnevZkcAAAAAElFTkSuQmCC">Netflix</A>
            <DT><A HREF="https://www.youtube.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="https://www.youtube.com/s/desktop/4151fd0f/img/favicon.ico" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAtklEQVQ4T2NkoBAwUqifAW7AfwYGAaBhBlADHXAYfAAqfgGo8QOIDTYAqDkBSM0n0TWJQM0LGIGaQbaeJ1EzTLkhyIAAIG89mQYkggxoAGqux2rAgwdAzwF9dwDmdQxVjfgN+A80HgQ2bmRgKChgYAAZiAqINODgQYhLSDYApAFk84YNuIII7ALcgSgATBofwNGNC4ADkbJoBBlNUUKCuQ0tKYNcBUra6AAWn6hJGZ8nCclRnBsBzJ03KZWC+NsAAAAASUVORK5CYII=">YouTube</A>
            <DT><A HREF="https://pluto.tv/?utm_source=google&utm_medium=textsearch&utm_campaign=1000710&utm_content=10000162&gclid=Cj0KCQjw37iTBhCWARIsACBt1IxSbMUhfgR3zcpVN3I4eJAHu8DBWzBUoS6Pw7rZlD4Af_SVeVETQKsaAn-vEALw_wcB" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Pluto TV - Drop in. Watch Free.</A>
            <DT><A HREF="https://www.vuemastery.com/courses/intro-to-vue-3/list-rendering-vue3" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.vuemastery.com/courses/intro-to-vue-3/list-rendering-vue3" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAB+ElEQVQ4jd1SPWhTURg99ycvea9JbYdG8IViUaGVgkVFQRCFLgoGilhc/JscxBShICgOz610dnJRh4rUMdgiKB0CkkBA8CdoQKJSbElq2vy8m/a+d+91qqgt7nqm7xzOOZzhA/4/eJUrMc94dItevOps599i1KsJD6+/n/0tvOBxTSNPvOL1wb8WTBYnB0VIJ9qKTmXyme5NvRVfGxMhT7cNn/5z3U/iGY+KgEyLkNsi4HtCbd0AgEw+0y1CPiVCDhGw9FLBP/VrAdk8LuVunaFGZRtlAd5D4STtFiNkRBlzATB3l/N17DzUC2LR91HbPnL/sCf2j49bDADSWc/R3DyVkvQtzq7g28cV7BhJRjc0HQ4NPd9cllb54WdYXXHQXXayI/Va6VHuVa1UUhQAdAzX1gM2VC/4UA2Fdlmg9sGHCNmoH7CuL8+WwMDQyLfQXgWEitw+PeelAICdnPNSytDHsqls8bwKoslLpRSTVdljHeiD+OSjnauCMTZjcWtf4OuIGYjbirLey3tPZNnAxdF7AI7KhRp0VW5QwsYMNW+5JOeIxSGLdVCJimNbaQLm6Lo8xlIOSIIPf+1nL6hR6iaX2iWVdZcr01+Yf1B6c3xo1nFsl5SabrRD3Z5E7GBhfqZpd8idCOeuWmy5nOndURW+2+65/jH8AP2T3WN8EpmlAAAAAElFTkSuQmCC">List Rendering - Intro to Vue 3 | Vue Mastery</A>
            <DT><A HREF="https://www.twitch.tv/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="https://assets.twitch.tv/assets/favicon-16-52e571ffea063af7a7f4.png" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACpSURBVHgB1ZHBDQIhEEX/GGvDNqxA3YNn2QrMagVGrxYgVmApe9QCdhQMEUdWIHvanwCTybzPDBAC7RVvOkAjU0tDNI3Bi0sa3s3e50TCpXIG/2B/k4y/DIZoBAbhj/j40RYYSFn4vHYPXxcbePjeoq4MaZsjuzWKOQbYlm+n1zp+ch2jqa60Qs4IPzBwCOG0gYQNzWUNxUA/Uh+U1YGbNQH3aqtY59Y+AYmPQ7sreL+6AAAAAElFTkSuQmCC">Twitch</A>
            <DT><A HREF="https://www.primevideo.com/region/eu/?ref_=dv_web_force_root" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Prime Video</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">twitch</H3>
            <DL><p>
                <DT><A HREF="https://placeit.net/c/design-templates/stages/twitch-overlay-maker-with-a-futuristic-panel-look-1245c?textText_T1=LINSPEC&textText_T4=twitch.tv%2Fw4lt3rc&textText_T5=%40linspec1&textText_T6=%40linspec1&pos-size_Livecam%20Frame%20Color=0.7427_0.6043_0.2293_0.2441_d&pos-size_Overlay%20Frame%20=-0.0040_0.0261_1.0080_0.9336_d&colorFolder_Livecam%20Frame%20Color=%238f00ff&colorFolder_Overlay%20Frame%20=%2333048e" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Placeit - Twitch Overlay Maker with a Futuristic Panel Look</A>
            </DL><p>
        </DL><p>
        <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725972321">Programacion</H3>
        <DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971499">Python</H3>
            <DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971439">APIS</H3>
                <DL><p>
                    <DT><A HREF="https://www.alphavantage.co/documentation/#" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">API Alpha Vantage</A>
                    <DT><A HREF="https://rapidapi.com/marketplace" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">API Marketplace  | RapidAPI</A>
                    <DT><A HREF="https://pypi.org/project/streamlit/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Streamlit · PyPI</A>
                    <DT><A HREF="https://api1.binance.com/sapi/v1/system/status" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">https://api1.binance.com/sapi/v1/system/status</A>
                    <DT><A HREF="https://rapidapi.com/hub" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">API Marketplace  | RapidAPI</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">info</H3>
                <DL><p>
                    <DT><A HREF="https://conda-forge.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">conda-forge | community driven packaging for conda</A>
                    <DT><A HREF="https://uniwebsidad.com/libros" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Libros y manuales sobre HTML, CSS, PHP, JavaScript y Symfony</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971172">Binance</H3>
                <DL><p>
                    <DT><A HREF="https://binance-docs.github.io/apidocs/futures/en/#get-current-multi-assets-mode-user_data" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Binance API - Get Current Multi-Assets</A>
                    <DT><A HREF="https://medium.com/analytics-vidhya/futures-trading-with-python-binance-d738c71e17b5" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Futures Trading with python-binance</A>
                    <DT><A HREF="https://python-binance.readthedocs.io/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Binance API — python-binance 0.2.0 documentation</A>
                    <DT><A HREF="https://testnet.binance.vision/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Binance Spot Test Network</A>
                    <DT><A HREF="https://realpython.com/python-f-strings/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Python 3&#39;s f-Strings</A>
                    <DT><A HREF="https://sammchardy.github.io/binance-order-filters/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Filtros de orden de Binance</A>
                    <DT><A HREF="https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">binance-spot-api-docs</A>
                    <DT><A HREF="https://www.trbinance.com/apidocs/#iceberg_parts" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Explicacion Filtros Binance</A>
                    <DT><A HREF="https://binance-docs.github.io/apidocs/spot/en/#change-log" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Change Log – Binance API Documentation</A>
                    <DT><A HREF="https://github.com/sammchardy/python-binance" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">API Binance Exchange</A>
                    <DT><A HREF="https://testnet.binancefuture.com/en/futures/BTCUSDT" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Testnet Binance Futures</A>
                    <DT><A HREF="https://python-binance.readthedocs.io/en/latest/index.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Welcome to python-binance v1.0.12 — python-binance 0.2.0 documentation</A>
                    <DT><A HREF="https://python-binance.readthedocs.io/en/latest/" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">Binance API — python-binance 0.2.0 documentation</A>
                </DL><p>
                <DT><A HREF="https://api1.binance.com/api/v3/depth?symbol=ADAUSDT" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">https://api1.binance.com/api/v3/depth?symbol=ADAUSDT</A>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">DJANGO</H3>
                <DL><p>
                    <DT><A HREF="https://www.youtube.com/watch?v=KdPf-pNK1s0&list=PLEsfXFp6DpzQSEMN5PXvEWuD2gEWVngCZ" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">(246) Try Django 1.10 - 1 of 40 - Welcome - YouTube</A>
                    <DT><A HREF="http://www.protutorialplus.com/django-listview" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Django ListView Tutorial with Example</A>
                    <DT><A HREF="https://docs.djangoproject.com/en/3.2/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Django documentation | Django documentation | Django</A>
                    <DT><A HREF="https://docs.djangoproject.com/en/3.2/ref/forms/widgets/#textinput" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Widgets | Django documentation | Django</A>
                    <DT><A HREF="https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Creating forms from models | Django documentation | Django</A>
                    <DT><A HREF="https://docs.djangoproject.com/en/3.2/topics/forms/formsets/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Formsets | Django documentation | Django</A>
                    <DT><A HREF="https://djangocentral.com/django-ajax-with-jquery/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Django + AJAX : How to use AJAX in Django Templates - Django Central</A>
                </DL><p>
                <DT><A HREF="https://realpython.com/python-pyqt-database/" ADD_DATE="1670704449" LAST_MODIFIED="1724671971">Handling SQL Databases With PyQt: The Basics – Real Python</A>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971439">Lectura</H3>
                <DL><p>
                    <DT><A HREF="https://blog.quantinsti.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Quantitative Finance &amp; Algo Trading Blog by QuantInsti</A>
                    <DT><A HREF="https://vim-bootstrap.com/#tagline" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Your configuration generator for NeoVim and Vim - Vim Bootstrap</A>
                    <DT><A HREF="http://www.soudegesu.com/en/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Sou-Nan-De-Gesu</A>
                    <DT><A HREF="https://stocktwits.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Stocktwits - The largest community for investors and traders</A>
                    <DT><A HREF="https://www.investopedia.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Investopedia: Sharper insight, better investing.</A>
                    <DT><A HREF="https://learngitbranching.js.org/?locale=es_ES" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Learn Git Branching</A>
                    <DT><A HREF="https://duckduckgo.com/?q=owerwacht+map+bagroud+hd&t=brave&iax=images&ia=images" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">owerwacht map bagroud hd at DuckDuckGo</A>
                    <DT><A HREF="https://www.atlassian.com/git/tutorials/saving-changes/git-commit" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">Git Commit | Atlassian Git Tutorial</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">NGINX</H3>
                <DL><p>
                    <DT><A HREF="https://zach.codes/roll-your-own-ngrok/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Roll your own ngrok in 15 minutes</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971452">Flask</H3>
                <DL><p>
                    <DT><A HREF="https://flask.palletsprojects.com/en/2.0.x/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Flask</A>
                    <DT><A HREF="https://github.com/lingthio/Flask-User" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://github.com/lingthio/Flask-User" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABcUlEQVQ4jY3TvWpVURAF4LXvvUmuIkEsLLQKgiAW/qAkNvoUFraCDxMlqEUCghZaiyKCjU3wBewEBTUpFEvBGJEkfjZz8HAw4sCG2XvNmv+dJEFLCS7hAT5gGz9Kv4/F7CeYwUoROvlVp5NtLGPUJ44wh+f+Xx5XwFHn5E4BL3EN69jCBj6W/qqwF2W73JGX8BO7WK23CY5jWucYZgu7XbbfcW6S5EaS2apoF+Mke621T70WfUYrbDfJOMnBJNeDd9WobZzs9aU/mdbdsYBvxXmdqg82MbPvmP44G+NtOfg6StKSSHIoyYF+5L+QW5JpkvniTUZJNgs/kmSxtaaaOCxh0lqTZCnJ0Qq6EdyrdLaqjFP/yOA03mCvyl4LztflLp6U/hRnBsSHvX7t1OjPdgZrBVzArVqohZ6DE4N1hpXhKq/jPa7i4iD1Kb70nDwrzmho9KhndLiHzVefdrDabeVwPJ1+GTcx7b3N1S+8MuT8Bs9NR9kw0z0NAAAAAElFTkSuQmCC">lingthio/Flask-User: Customizable User Authorization &amp; User Management: Register, Confirm, Login, Change username/password, Forgot password and more.</A>
                    <DT><A HREF="https://github.com/andymccurdy/redis-py" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">andymccurdy/redis-py: Redis Python Client</A>
                    <DT><A HREF="https://docs.celeryproject.org/en/latest/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Celery - Distributed Task Queue — Celery 5.1.2 documentation</A>
                    <DT><A HREF="https://flask-sqlalchemy.palletsprojects.com/en/2.x/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Flask-SQLAlchemy</A>
                    <DT><A HREF="https://flask-login.readthedocs.io/en/latest/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Flask-Login</A>
                    <DT><A HREF="https://itsdangerous.palletsprojects.com/en/2.0.x/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ItsDangerous — ItsDangerous Documentation (2.0.x)</A>
                    <DT><A HREF="https://jinja.palletsprojects.com/en/3.0.x/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Jinja — Jinja Documentation (3.0.x)</A>
                    <DT><A HREF="https://wtforms-components.readthedocs.io/en/latest/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">WTForms-Components — WTForms-Components 0.1 documentation</A>
                    <DT><A HREF="https://github.com/mbr/flask-bootstrap" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">mbr/flask-bootstrap: Ready-to-use Twitter-bootstrap for use in Flask.</A>
                    <DT><A HREF="https://github.com/flask-debugtoolbar/flask-debugtoolbar" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">flask-debugtoolbar/flask-debugtoolbar: A toolbar overlay for debugging Flask applications</A>
                    <DT><A HREF="https://github.com/dusktreader/flask-praetorian" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">dusktreader/flask-praetorian: Strong, Simple, and Precise security for Flask APIs (using jwt)</A>
                    <DT><A HREF="https://github.com/Flask-Middleware/flask-security/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Flask-Middleware/flask-security: Quick and simple security for Flask applications</A>
                    <DT><A HREF="https://nickjanetakis.com/blog/15-useful-flask-extensions-and-libraries-that-i-use-in-every-project" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">15 Useful Flask Extensions and Libraries That I Use in Every Project — Nick Janetakis</A>
                    <DT><A HREF="https://www.educba.com/flask-extensions/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Flask Extensions | Guide to List of Flask Extensions</A>
                    <DT><A HREF="https://flask-wtf.readthedocs.io/en/0.15.x/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Flask-WTF — Flask-WTF Documentation (0.15.x)</A>
                    <DT><A HREF="https://wtforms.readthedocs.io/en/2.3.x/forms/#the-form-class" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Forms — WTForms Documentation (2.3.x)</A>
                    <DT><A HREF="https://www.educba.com/flask-get-post-data/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Flask get post data | Learn How to get POST data in Flask?</A>
                    <DT><A HREF="https://github.com/redis/redis-py" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">andymccurdy/redis-py: Redis Python Client</A>
                    <DT><A HREF="https://docs.celeryq.dev/en/latest/" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">Celery - Distributed Task Queue — Celery 5.1.2 documentation</A>
                    <DT><A HREF="https://palletsprojects.com/p/jinja/" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">Jinja</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971172">Analisis</H3>
                <DL><p>
                    <DT><A HREF="https://pypi.org/project/ccxt/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CCXT</A>
                    <DT><A HREF="https://ccxt.readthedocs.io/en/latest/manual.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CCXT  Documentation</A>
                    <DT><A HREF="https://numpy.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">NumPy</A>
                    <DT><A HREF="https://pandas.pydata.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Pandas</A>
                    <DT><A HREF="https://pandas-datareader.readthedocs.io/en/latest/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Pandas-datareader</A>
                    <DT><A HREF="https://github.com/bukosabino/ta" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">TA</A>
                    <DT><A HREF="https://github.com/mrjbq7/ta-lib" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">TA-Lib</A>
                    <DT><A HREF="https://github.com/twopirllc/pandas-ta" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">twopirllc/pandas-ta: Technical Analysis Indicators - Pandas TA is an easy to use Python 3 Pandas Extension with 130+ Indicators</A>
                    <DT><A HREF="https://github.com/twopirllc/pandas-ta/tree/main/pandas_ta" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">pandas-ta/pandas_ta at main · twopirllc/pandas-ta</A>
                    <DT><A HREF="https://docs.ccxt.com/en/latest/manual.html" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">CCXT  Documentation</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971172">CCXT</H3>
                <DL><p>
                    <DT><A HREF="https://github.com/ccxt/ccxt/blob/master/examples/py/binance-conditional-orders.py" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ccxt/binance-conditional-orders.py at master · ccxt/ccxt</A>
                    <DT><A HREF="https://github.com/ccxt/ccxt/blob/master/examples/py/binance-futures-margin.py" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ccxt/binance-futures-margin.py at master · ccxt/ccxt</A>
                    <DT><A HREF="https://lightrains.com/blogs/how-create-binance-token" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">How to create and issue token on Binance Chain #BinanceToken</A>
                    <DT><A HREF="https://github.com/ccxt/ccxt/tree/master/examples/py" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ccxt/examples/py at master · ccxt/ccxt</A>
                    <DT><A HREF="https://github.com/ccxt/ccxt/issues?q=createOrder+quote++currency" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Issues · ccxt/ccxt</A>
                    <DT><A HREF="https://github.com/ccxt/ccxt/issues/9001" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">no attribute &#39;futures_create_order&#39; · Issue #9001 · ccxt/ccxt</A>
                    <DT><A HREF="https://github.com/ccxt/ccxt/blob/master/examples/py/async-binance-futures-vs-spot.py" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ccxt/async-binance-futures-vs-spot.py at master · ccxt/ccxt</A>
                    <DT><A HREF="https://ccxt.readthedocs.io/en/latest/index.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CCXT — ccxt 1.56.34 documentation</A>
                    <DT><A HREF="https://docs.ccxt.com/en/latest/index.html" ADD_DATE="1667664395" LAST_MODIFIED="1725971172">CCXT — ccxt 1.56.34 documentation</A>
                </DL><p>
                <DT><A HREF="https://www.python.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="https://www.python.org/static/favicon.ico" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACe0lEQVQ4T3WTX0iTURjGz5nWhuVNERXVTd2UEhEUURdTLA1rpQXCLroKuygkr6QiMLuIJJOkG4suujC6GVRoMCozY2E6Yg4KRMpGc2WmG8P9+f6cc77Tc/avbdIHv33n4jzP+7zv946Ssqelf/w5M0ynJcwNnBmEmyYRpq4zTXs0OXjpGq7rQORltNzAdWdUjnQdJU09LyA2iGAmyRoZxD/YsQf350HqvwbNt7yyWJQ5QyylpQwaIPwClkoMWgY+dFuM7eSmRpHWZmrJSq4nKwTi29ba2yyRTQyDZryC4HfB4Oz9ibeCsQaOSiIXVUXOVxacFbpUBjLc5pU8pTM91Weved9LW+/5pIpYLCo+59VI5A08vtovv58cJTxNJEvHbLVTh+ipvrGMQaZ6rt9sEjPTN350bqTeQfxwOdB4eON6cYVwzFCkCd372UlP3H4lRS6BEumJmPfn1PDTSOBNHNU5kMAM+xprtm/md6nQHBkDpKD7547TppsjmsVNh4qdji97/A8uP0mEO93r7OxM5jIqqct5UfaMFjimfTDSSo91P5vBwHYrg9CY59zs8C53lV24ygUlJkInyZTlq677dYPWdw11WlL2cqSYGGh3yaWOl/kqqyur3tUiEuKb1q47L0Rfq010gK1gGzDkwnl/3uDPYtxjszRJBIRMgxjg+fqDBY+0RydxDCkDG7CDKjUwOe+OliZAz8qAa4QeiKhNTALltAKiq/4LVui0Rnm6aHgw2DdL5KcdamhqE78pYe4L8VUGK8F6l6PC7KkkqdrsJ0sTxq3Zj9PGUN3F6DiEMyBWWOXCnv47qJlsAltANVgDsFEkARbAIshOEs9fij3FuUNAOQ8AAAAASUVORK5CYII=">Doc  Python</A>
                <DT><A HREF="https://pypi.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="https://pypi.org/static/images/favicon.35549fe8.ico" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAD80lEQVRYR+1XS2sbVxiduXMf85TU2KZOoYVAA8ZGcWRMoZsQQ8kidJsuuyhd9QcVWrrvrnTRnTchpKROQVYeckxcHLCISZ26rl7zvDPTc91GKKqUjNwsstCF4c7iu9853+POnE/XzrB2d3ffI0T7yjTFFUJ0NwiSO3Ecf7eysrI9rTu96IG9vT1hGNoNTTOuOo655jjOBV3XTTx6nudRGMa/+37/Hog8wPu3IPOsiO9XEoBjHdFeEUJcY4xdKpedy7pueIjaBi7DM8CAbZrnWZBleRAE0eMg8JtxLO+22+3v19fX/UlkxhLY3t6+WCpZ1xkTq55XWqPUWNS0vGQY1BoGHecURLQsyxLsPex/hWFYD4LwUb8f/Ly8vLyJ8+nwuQGBer2+UC6XPzFNeokxsyYEvwjDOYCXCEIuks5Rm3/IpH6aZm28P/X96Nc4DndOTtq3a7VaQ9nrzWbzM8/zPhCCVZHqVVT0PCH0HIDpWUAnnQGBPElkR9OyozhOHodhdLfb7T9HjR/dNIU5T5nxbqVSfsfAepPAo77iOJK+H/SzTHsOIm19f/+3Q8s0SypdnDOSIWuoE7GwDIO8ES5Spjl6IUQPSVSTI/EppSzv9Xpt/eBg/8Bz3fcVASllKGWWoOEMxgVBk6eoPzVx4V/XfKNM0YBaFMWh8oHLpLKaKgLwZXNEquyPj49bAwLDDhQZXKG+lEmCZHDLtoiqIRxwNOfEEqlzCRauogSwjmBUAJJzwW3b/s8NmkhghEwWxVFPJmlqUGY5tqXlMECrCErp6e1A5hBwFgOf4F0q/oxx4rouru7klipEYJiMTKWMwqSjIjUt0+OMa8QwclwtRJ73AEYrlYoDYoUaeWoCw2TwuQ18fF0cr6zh++Ghtqd1nWb9LwIKyPf97vzCeQ9NNQ3uwHZGYJaBWQZmGZhl4O3IwJMnezcd217GX+2cQUihv9iLj/lZ/wWQDHGapn9Asjf1nZ2Hn1uWuQKhcRk69EMonznIpkJKeBoC0AvATLvY/8Tg8ABnG1Bp9wdyW80ClhDXmWCrrmOtIRmLUDUYQogaQsb+7V5HQKkogAbYupiYWgCudzqdHZz7oVqttk5l+RgtfzoNUapdowavuq5VAwkPpiCivTQNjSPw72ACdZQHAD/pdrv3VcQQoD9hMPllFO+VA4eaB8H8Buf0quC85jj2BQhWNQ8qkUpeEMDYpvxCfOaqtiGixGgW3MO+eXR09OPGxoacJBgKTzxbW1tzGGC+AJGPTZN/ZNtiHoIonF9YdEBA9vv9QwA+RF1vtVqtbwDaK6JSChMYdtZoNGoYG75EW33qet6zKIo2oUW/XlpaOiwCOmzzN6rOuZHnUKZGAAAAAElFTkSuQmCC">PyPI,org</A>
                <DT><A HREF="https://docs.python.org/3.8/tutorial/classes.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">9. Classes — Python 3.8.11 documentation</A>
                <DT><A HREF="https://www.investopedia.com/articles/technical/02/010702.asp" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">What Is Stock Volume? How to Improve Your Trading</A>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">VSCODE</H3>
                <DL><p>
                    <DT><A HREF="https://github.com/kasecato/vscode-intellij-idea-keybindings#readme" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">kasecato/vscode-intellij-idea-keybindings: Port of IntelliJ IDEA key bindings for VS Code.</A>
                </DL><p>
                <DT><A HREF="http://docs.peewee-orm.com/en/latest/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">peewee — peewee 3.14.4 documentation</A>
                <DT><A HREF="https://www.fmlabs.com/reference/default.htm" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Technical Indicator Reference</A>
                <DT><A HREF="https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#field-lists" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">reStructuredText Primer — Sphinx documentation</A>
                <DT><A HREF="https://www.tutorialspoint.com/python/dictionary_update.htm" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Python dictionary update() Method</A>
                <DT><A HREF="https://www.programcreek.com/python/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Python Code Examples</A>
                <DT><A HREF="https://www.djangoproject.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">The web framework for perfectionists with deadlines | Django</A>
                <DT><A HREF="https://www.tutorialspoint.com/index.htm" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Biggest Online Tutorials Library</A>
                <DT><A HREF="https://www.youtube.com/watch?v=71EU8gnZqZQ" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Python Flask Authentication Tutorial - Learn Flask Login - YouTube</A>
                <DT><A HREF="https://getbootstrap.com/docs/5.1/getting-started/introduction/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Introduction · Bootstrap v5.1</A>
                <DT><A HREF="https://www.programcreek.com/python/example/104636/wtforms.fields.SelectField" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Python Examples of wtforms.fields.SelectField</A>
                <DT><A HREF="https://tailwindcss.com/docs" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Documentation - Tailwind CSS</A>
                <DT><A HREF="https://developer.mozilla.org/es/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">MDN Web Docs</A>
                <DT><A HREF="http://www.djangobook.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:http://www.djangobook.com/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADIklEQVQ4jXWTX2yTZRTGn/N979e6jRaasDkoXQdLNzdwBbrRwSAhDEgmUC8IxGxoZNGRmLj458KYoDHG6I3ETBRqTMBg0LAQFUmEiyUaI/+MAzYwGzE6L8ARO1jWde36te/7eLMRXPR3e57nnJyT5wj+jQCg3VTbrqEPYypdCuXQLi1z9dSkF5YldpnvlnZznRi8fQeAZQOwZo0CwAZAVPg+DgWXNe3dvstXXl7h+2v870VPtrX7asI1C/4cv1tttLnDsYlLAIj5EJuVWhX8PvFKtybJi9cHdHB7XHOWRVvWaKytfol7+uzYnq0LFWIrHgcAj8cDEdkk0388hXsTsdS9cTGkyeSmJZPN4stzZ0w6M4VCviAweFZuvNgBmqXKozxDpIHRBkU3j5Y1zahfVoWVkXpaIuIoJdlcFkf6PkehWBTXzTMQCEQ3rt6GUEUlgGjYOPE6Y60Om96Tx4qcR//ln8zSretIkpPptFnQupI3fxt5sJKK1jVg8MZV7Gh7Aj0d++3UxH0+98arCIdC+PC1t4UkDAwKxQInpzNS4vUyefqkDAz/ykw2A+ur94+K2ErWR9eKNgbHvzkl3/adkJHRUQEAQ4pQAEIcpTCZycjloWvy8r4u+e6jz0S99UkvWSxCAFgiWOjzCwDOFFwhCZIgCMuykJvJYdWKCC6d+Bqpifs4/MUxWNvirRqOo/t/vqBFRA7s7sChQ0l0ticoIvA4DmzLpm3bnHFd1ASrqJTCjwNXeKb/HBHfv5uqpZaILecL7x40t++OFeYONJPP89T5syaS2ExjDG+N/s7KLU3m4rVfHmgE9Us+dfx+LTBL3Olswr94MYLlj8Jj2ci7LkduDsnzT3cxefA9XBm6ig2dCSkJBFBbVQ2v44Hi8Fi3YIwA4N/YGE+nM4l0KrUcSrXA6NAze/fhyOvv2JaIHD97WgNwTVEnBwevh0Fdgtn8z/3EbJwhpesbDng2PMadPV08f+GHwptHPyhazTVUzXW9cxo+5JnDeqih12mO9KChchjRENEYMva6SBKAA0DNH/q/xLp3lT7S2tBZtqmx7b/q/wD384+/iH+2NQAAAABJRU5ErkJggg==">The Django Book</A>
                <DT><A HREF="http://www.pygtk.org/pygtk2tutorial-es/index.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Tutorial de PyGTK 2.0 versión 2.3</A>
                <DT><A HREF="https://recursospython.com/guias-y-manuales/decoradores/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Decoradores - Recursos Python</A>
                <DT><A HREF="https://www.tutorialspoint.com/python/python_date_time.htm" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Python - Date &amp; Time - Tutorialspoint</A>
                <DT><A HREF="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">The Flask Mega-Tutorial Part II: Templates - miguelgrinberg.com</A>
                <DT><A HREF="https://tailwindcss.com/docs/installation" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Documentation - Tailwind CSS</A>
                <DT><A HREF="https://pynative.com/python-timestamp/#h-convert-timestamp-to-datetime-format" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Python Timestamp With Examples – PYnative</A>
                <DT><A HREF="https://djangobook.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">The Django Book</A>
                <DT><A HREF="https://pygobject.readthedocs.io/en/latest/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Tutorial de PyGTK 2.0 versión 2.3</A>
            </DL><p>
            <DT><A HREF="https://langserver.org/#implementations-server" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Langserver.org</A>
            <DT><A HREF="https://github.com/jakewies/.dotfiles/blob/main/nvim/.config/nvim/init.vim" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">.dotfiles/init.vim at main · jakewies/.dotfiles · GitHub</A>
            <DT><A HREF="https://www.jakewiesler.com/blog/getting-started-with-vim" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Getting Started With Vim - A Practical Guide</A>
            <DT><A HREF="https://learnvimscriptthehardway.stevelosh.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Learn Vimscript the Hard Way</A>
            <DT><A HREF="https://www.typingclub.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Learn Touch Typing Free - TypingClub</A>
            <DT><A HREF="https://polyhaven.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Poly Haven</A>
            <DT><A HREF="https://www.luisan.net/blog/diseno-grafico/20-bancos-de-imagenes-gratis-de-alta-resolucion-para-tu-web" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">20 bancos de imágenes gratis de alta resolución para tu web</A>
            <DT><A HREF="https://www.siteslike.com/similar/xnxx.com" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Sites Like Xnxx.com 50 (Xnxx.com) alternatives</A>
            <DT><A HREF="https://nicepage.com/es/ht/1381816/arquitectos-mejor-valorados-plantilla-html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Arquitectos mejor valorados Plantilla HTML</A>
            <DT><A HREF="https://nicepage.com/es/html-templates/preview/arquitectos-mejor-valorados-1381816?device=desktop" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Arquitectos mejor valorados #html-templates-es-seo-one-item-suffix Live Demo</A>
            <DT><A HREF="https://www.bensound.com/royalty-free-music" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Royalty Free Music - Bensound</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971452">html templates</H3>
            <DL><p>
                <DT><A HREF="https://docs.djangoproject.com/es/3.1/topics/db/models/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Models | Documentación de Django | Django</A>
                <DT><A HREF="https://symfonycasts.com/screencast/symfony4/flex-recipes#play" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Symfony Flex &amp; Aliases &gt; Stellar Development with Symfony 4 | SymfonyCasts</A>
                <DT><A HREF="https://www.facebook.com/instantgames/play/306645160322472/?source=www_games_hub" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">(20+) Facebook</A>
                <DT><A HREF="https://www.youtube.com/watch?v=LBr8AssBW6o" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">(364) ¡NOS MUDAMOS! BUSCANDO PISO en una CIUDAD CHINA - YouTube</A>
                <DT><A HREF="https://www.pngegg.com/es/png-bypke/download" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Descarga gratis | Icono de marca de verificación de etiqueta, material de etiquetas de etiqueta de pincho de marca de verificación, sí sin ilustración, texto, etiqueta png | PNGEgg</A>
                <DT><A HREF="https://github.com/tpope?tab=repositories" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">tpope (tpope) / Repositories</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971452">tools</H3>
            <DL><p>
                <DT><A HREF="https://www.pluralsight.com/guides/install-npm-packages-from-gitgithub" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Install NPM Packages from GitHub | Pluralsight</A>
                <DT><A HREF="https://lenguajejs.com/javascript/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Lenguaje Javascript - Javascript en español - Lenguaje JS</A>
                <DT><A HREF="https://www.skypack.dev/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Skypack: search millions of open source JavaScript packages</A>
                <DT><A HREF="https://lenguajejs.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Lenguaje Javascript | Documentación sobre programación web - Javascript en español - Lenguaje JS</A>
                <DT><A HREF="https://mdbootstrap.com/docs/vue/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bootstrap 5 &amp; Vue - Free Material Design UI KIT</A>
                <DT><A HREF="https://transform.tools/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Transform</A>
                <DT><A HREF="https://packagephobia.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Package Phobia</A>
                <DT><A HREF="https://lenguajecss.com/postcss/plugins/autoprefixer/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Autoprefixer: Prefijos CSS - CSS en español - Lenguaje CSS</A>
                <DT><A HREF="https://hue.tools/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">hue.tools</A>
                <DT><A HREF="https://es.keysfan.com/tools.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Tools Software Key for Study and Work - KeysFan</A>
                <DT><A HREF="https://vitepress.vuejs.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">VitePress | Vite &amp; Vue Powered Static Site Generator</A>
                <DT><A HREF="https://element-plus.org/es-ES/#/es" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Un Framework UI para la web basado en Vue 3 | Element Plus</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971498">Cursos</H3>
            <DL><p>
                <DT><A HREF="http://www.phptherightway.com/#top" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">PHP: The Right Way</A>
                <DT><A HREF="https://www.udemy.com/courses/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Best Online Courses | Udemy</A>
                <DT><A HREF="https://es.khanacademy.org/welcome" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Panel | Khan Academy</A>
                <DT><A HREF="http://code.tutsplus.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Tuts+ Free Code Tutorials</A>
                <DT><A HREF="https://www.tutorialspoint.com/laravel/laravel_facades.htm" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Laravel Facades</A>
                <DT><A HREF="https://www.khanacademy.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Dashboard | Khan Academy</A>
                <DT><A HREF="file:///Users/waltercervini/Downloads/cursos/cursojquery/index.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Curso de jQuery - Uno de piera</A>
                <DT><A HREF="https://www.codeschool.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Learn to Code by Doing - Code School</A>
                <DT><A HREF="http://it-ebooks.info/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">IT eBooks - Free Download - Big Library</A>
                <DT><A HREF="https://www.udemy.com/courses/search/?q=jquery&p=1&price=price-free&view=grid" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">jquery courses</A>
                <DT><A HREF="http://www.iebschool.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">IEBS - La Escuela de Negocios de la Innovación y los Emprendedores.</A>
                <DT><A HREF="http://escuela.it/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">EscuelaIT - Formación profesional en el área IT</A>
                <DT><A HREF="https://scotch.io/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Scotch ♥ Developers bringing fire to the people.</A>
                <DT><A HREF="http://coolvillage.es/unidades-de-medida-en-css/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Unidades de medida en CSS</A>
                <DT><A HREF="https://www.udemy.com/courses/search/?q=javascript+for+beginners&sort=language&price=price-free&view=grid" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">javascript for beginners courses</A>
                <DT><A HREF="http://entredesarrolladores.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">entre Desarrolladores</A>
                <DT><A HREF="https://www.faztweb.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Fazt | Aprende a crear la web por ti mismo</A>
                <DT><A HREF="https://fullstackopen.com/es/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Full stack open 2022</A>
                <DT><A HREF="https://sebhastian.com/javascript-tutorials/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">JavaScript tutorials - Nathan Sebhastian</A>
                <DT><A HREF="https://escuelavue.es/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Curso de Vue, JavaScript y mucho más. Aprender Vue y desarrollo Web en Escuela Vue</A>
                <DT><A HREF="https://losapuntesdemajo.vercel.app/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Apuntes de Majo</A>
                <DT><A HREF="https://phptherightway.com/#top" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">PHP: The Right Way</A>
                <DT><A HREF="https://www.udemy.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Best Online Courses | Udemy</A>
                <DT><A HREF="https://es.khanacademy.org/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Panel | Khan Academy</A>
                <DT><A HREF="https://code.tutsplus.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Tuts+ Free Code Tutorials</A>
                <DT><A HREF="https://www.pluralsight.com/codeschool" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Learn to Code by Doing - Code School</A>
                <DT><A HREF="https://it-ebooks.info/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">IT eBooks - Free Download - Big Library</A>
                <DT><A HREF="https://www.udemy.com/courses/search/?price=price-free&q=jquery&view=grid" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">jquery courses</A>
                <DT><A HREF="https://www.iebschool.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">IEBS - La Escuela de Negocios de la Innovación y los Emprendedores.</A>
                <DT><A HREF="https://escuela.it/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">EscuelaIT - Formación profesional en el área IT</A>
                <DT><A HREF="https://www.univision.com/explora/aumenta-tus-conocimientos-en-programacion-con-estos-excelentes-cursos-online-gratuitos" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Aumenta tus conocimientos en programación con estos excelentes cursos online gratuitos - TechTear</A>
                <DT><A HREF="https://www.digitalocean.com/community" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Scotch ♥ Developers bringing fire to the people.</A>
                <DT><A HREF="https://coolvillage.es/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Unidades de medida en CSS</A>
                <DT><A HREF="https://entredesarrolladores.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">entre Desarrolladores</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">github</H3>
            <DL><p>
                <DT><A HREF="https://github.com/apvarun/awesome-bun" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">GitHub - apvarun/awesome-bun: ⚡️ A curated list of awesome things related to Bun</A>
                <DT><A HREF="https://github.com/vuejs/awesome-vue#icons" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">GitHub - vuejs/awesome-vue: 🎉 A curated list of awesome things related to Vue.js</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Online editors</H3>
            <DL><p>
                <DT><A HREF="https://runkit.com/linspec/62dcbbcc8c805300084dd3fd" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">untitled | RunKit</A>
                <DT><A HREF="https://blockchain.info/ticker" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">https://blockchain.info/ticker</A>
                <DT><A HREF="https://www.napkin.io/dashboard" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">linspec - Napkin</A>
                <DT><A HREF="https://mockapi.io/projects" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">mockAPI</A>
                <DT><A HREF="https://www.executeprogram.com/courses/modern-javascript" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Modern JavaScript</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Ajax</H3>
            <DL><p>
                <DT><A HREF="http://www.sergiopereira.com/articles/DeveloperNotes-Prototype-JS.pdf" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">DeveloperNotes-Prototype-JS.pdf (application/pdf Objeto)</A>
                <DT><A HREF="http://demo.qooxdoo.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ajax Frm</A>
                <DT><A HREF="https://www.sergiopereira.com/articles/DeveloperNotes-Prototype-JS.pdf" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">DeveloperNotes-Prototype-JS.pdf (application/pdf Objeto)</A>
                <DT><A HREF="https://qooxdoo.org/qxl.demobrowser/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">ajax Frm</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971439">Bases Datos</H3>
            <DL><p>
                <DT><A HREF="http://www.linuxnetworks.de/doc/index.php/News" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Linuxnetworks</A>
                <DT><A HREF="http://marcelosoft.blogspot.com/2008/10/cmo-conectarse-oracle-desde-python-en.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">El Blog de Marcelo!: Cómo Conectarse a Oracle desde Python en Ubuntu</A>
                <DT><A HREF="https://unix.stackexchange.com/questions/130877/anyone-know-a-good-gui-to-mariadb" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">mysql - Anyone know a good gui to MariaDB? - Unix &amp; Linux Stack Exchange</A>
                <DT><A HREF="http://www.mysqlya.com.ar/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:http://www.mysqlya.com.ar/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADl0lEQVQ4jWXTXUybZRiH8f/9vP0YpQgUXG0pTBjdgCIYwelQRtGAkqjbDjyYIWwyFGV4aPzKkjceaTQaiGwsg6gDWYgJZrAaICibg0WmbExhlRXEAaUVwkdhsH7Q5/Zgnhiv89/hRbgfsQoiFRL15555pyL/+B6zsYTAFmJiCSx4FgKDH/WMtqDltSusQpAKBsAEAAwIQqaxuqvz00MOW7UvsKX8OuWFZ3mDAcCeFEeFu62wJRgi347ONH/1yv53WUWQVEhiVRWkjhjf7/vkYlleevF7bQPy5z/9EkQCioYAANsRBiCfSDeLppoK8c2V8f7PDxUcZlUNEgBUnb/aeqQot/poQ1docVtq9TE60jGwEYyACEg06LF2N4jDj+7i9ipnRGqE/sjZH7/ofv3ZtxRj3ZnShsrSzyw7EH0q06JJjNXT7NI6Pn6xECeKs6iycDfZEgw0+IeXaw9ki6fTd2q0UsrkhLiC86u2H0RV2WO1IBL2JCMqHDZyjc/xwtomfdg/RkUZZi7PSkGf28uQoKbhSXk3FOGle2EZBjRvHHyyVuxLSy45PTDG3/02K7RCoGSPhcDEs4sb/PU1D0UloyzLShAgz9wyddyYwVYoInrGpjk/LblEaAR23vStoHtijgDQwdw0QDBBgFzjc1AE4SVHKnQGPRMzbvkDGLmzRKMzf0OryBQhpUSsXovuiXlshre5fK8VqQ/GM8LbSDMZEY5K5FlN2GczEYcinJpoQPfEPIKSWYAgmBRfjsWEgH+Ve91exOm15MwwE3RatsYbcHrIDY0iuDwnlaHRUIbJiJ7xWc5LSaYohFe4fauD++0phKiUnTdnAADle61ckJpEi5tBbvzJzQCo3G6BI9OM5a0w1v0B6cxJo1vzy5eV2w88vljpdFRNrGxg2OOjugPZeNhkBCmEXreXJu4s0Qv5u/gRqwlJxh1ov+ZhnTGGX85PlydbB+rFYnPN8IXR6TNNR5/TiPB2pHloks1xMeR4KBFj8ysshMId12cQo1Uo1xzPbu9q5NSx5zVdo1PNK1+euApWVQEgVu37vf/iX+tc3zkcjTKHK9suS1SfiqKuRRrfbosG7oUilzy+6IXpNf7AdaMfQOy/FmAVAoDhzc5fGr+f9IfXJfNJ13UubXBFS5t6ZU3HEE+thXjgtj98rH248T6GAAD63841Z4tfdWYfL7JbnDoFKQBDQnhHPP5Lza6xVrTX/WfnfwDAH67Nq0nPyQAAAABJRU5ErkJggg==">MySQL Ya</A>
                <DT><A HREF="https://www.linuxnetworks.de/doc/index.php/News" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Linuxnetworks</A>
                <DT><A HREF="https://www.mysqlya.com.ar/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">MySQL Ya</A>
                <DT><A HREF="https://sites.google.com/site/kjalleda/mysqlfailover" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Kishore Jalleda - Mysql failover with Heartbeat and MON</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725970839">convertidores</H3>
            <DL><p>
                <DT><A HREF="http://www.prodraw.net/favicon/index.php" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Free Online Favicon.ico Icon Generator | Convert Image to ICO File</A>
                <DT><A HREF="http://www.icoconverter.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Online ICO converter</A>
                <DT><A HREF="https://www.icoconverter.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Online ICO converter</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971903">CSS</H3>
            <DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971708">Css Frameworks</H3>
                <DL><p>
                    <DT><A HREF="http://bulma.io/documentation/components/card/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bulma: a modern CSS framework based on Flexbox</A>
                    <DT><A HREF="https://purecss.io/forms/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Forms – Pure</A>
                    <DT><A HREF="http://concisecss.com/documentation/core" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Core—Concise CSS</A>
                    <DT><A HREF="http://milligram.io/#browser-support" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Milligram - A minimalist CSS framework.</A>
                    <DT><A HREF="file:///Users/waltercervini/websites/Materialize/materializecss.com/index.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Documentation - Materialize</A>
                    <DT><A HREF="https://bulma.io/documentation/components/card/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Bulma: a modern CSS framework based on Flexbox</A>
                    <DT><A HREF="https://concisecss.com/documentation/core" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Core—Concise CSS</A>
                    <DT><A HREF="https://milligram.io/#browser-support" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Milligram - A minimalist CSS framework.</A>
                </DL><p>
                <DT><A HREF="https://www.freedigitalphotos.net/images/search.php?search=movers" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Movers Stock Photos - Free Movers Images - FreeDigitalPhotos.net</A>
                <DT><A HREF="https://www.pexels.com/es-es/popular-searches/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Búsquedas populares</A>
                <DT><A HREF="https://css-tricks.com/snippets/css/a-guide-to-flexbox/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">A Complete Guide to Flexbox | CSS-Tricks</A>
                <DT><A HREF="file:///C:/Program%20Files%20(x86)/Ampps/www/carfact/vendor/almasaeed2010/adminlte/documentation/index.html#download" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">AdminLTE 2 | Documentation</A>
                <DT><A HREF="https://bootsnipp.com/snippets/featured/custom-search-input" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bootstrap Snippet Custom Search input using HTML CSS Bootstrap | Bootsnipp.com</A>
                <DT><A HREF="https://demo.agektmr.com/flexbox/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CSS Flexbox Please!</A>
                <DT><A HREF="http://www.dynamicdrive.com/style/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Dynamic Drive CSS Library- Practical CSS codes and examples</A>
                <DT><A HREF="http://www.dynamicdrive.com/dynamicindex1/indexb.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Dynamic Drive- CSS based menu scripts</A>
                <DT><A HREF="http://www.anieto2k.com/2006/03/23/efectos-css-increibles/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Efectos CSS increibles | aNieto2K</A>
                <DT><A HREF="http://www.exploding-boy.com/2005/12/15/free-css-navigation-designs/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Free CSS Navigation Menu Designs at ExplodingBoy</A>
                <DT><A HREF="https://lenguajecss.com/p/css/propiedades/grid-css" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://lenguajecss.com/p/css/propiedades/grid-css" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADBUlEQVQ4jV2Sy4tbdRTHP7/ffeXm5ubRScaM80otaacjOlYrKAUfTItaaBeCi67UjQvBbgQ3LnQx4MKuKgX/APeCFRFKtdCFMA6jjNDRMrZaMs3jJpMmk2SS+/q5CDNt/a7OOZzz5fs954jFz6592R6EH/lhrKQQAf9DHEaPFxTEAtO2jDBt61/rL87ndm5utf1h4LsjP0r0egFoApQCKTm0NA9inAexouhaqN0BYcXbO5ZPdPXDheT22r1O459W6C5MJpk5kmEYxKhYITXJ/NIUQgiUUiQ0QS0SrG1sk4JmueBU9axj1LO20YibgyPLr85y+cIJYPiI5sRjDlY2HvBdrctLKbM2dcip6rZueClL87B1frvX5eraHbxeQBTHCCkolqbZDWJeKNgczZo0RxH4IZmMXk0nZVXPm3oj55g1bJ2Nyi7nL/8+9uz1QdfgdR9aI6688xRHsxO0hmOCnJOsZ+ykp9sT095kun0fP8J0LZysRd4x+Pz9RQIFk6UpukHM8rQDwM4whCCk4Fr1jCFb+tmyGH367WYVQArojyI0IXjvtRIgAePhSRXsDEIIIzJJs/7GUrGvA6STsoEUADyZtfD9mFe++IWEpVF89jDdIOab0zNYmqQzDAFFzjWrADpAPmXVEYJmL+DGxeeYTBksfHAdHAOMHIwiUm/N0RxFDPwQlKKYsR4SOJZsmKaG3w+wkybH5vJ8/O5xfvjrAXPzKd4suQDcH0R0BwGmBq5ueAcEdspuOJaOPwi5udnkZMnl0oXnuaSG4z8QY3u3Oz6BH2JLgWXIFoDYX9DMJz/2Onuho4DFYpKXS2nefiZPYXaK7+92WfWG3AkkA69De32rV//qvHugACAaha3dVt+RboLVrQ6rfzS5cqPCzBlF148x/QDd96nc2mY6Vo39ObkffHi6vHJqqbhWcM0IYpBgmBrDSpP2+t/Uf73N6Na/4cmcsXrx3PGV/bkDC/v4+W47u77lLf9Z6535abN5LtwL4lPl7NUTs7lrTy88cf1seaL7aP9/78xBFa4JLPsAAAAASUVORK5CYII=">Grid CSS (Cuadrículas) | CSS en español</A>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971840">Herramientas Web</H3>
                <DL><p>
                    <DT><A HREF="http://viewdns.info/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ViewDNS.info - Your one source for DNS related tools!</A>
                    <DT><A HREF="http://placehold.it/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Placehold.it - Quick and simple image placeholders</A>
                    <DT><A HREF="http://dummyimage.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Dynamic Dummy Image Generator - DummyImage.com</A>
                    <DT><A HREF="https://mdbootstrap.com/material-design-for-bootstrap/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Material Design for Bootstrap 4 or 3</A>
                    <DT><A HREF="http://www.layoutit.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">LayoutIt! - Interface Builder for Bootstrap</A>
                    <DT><A HREF="https://mailtrap.io/settings" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">User Profile - Mailtrap</A>
                    <DT><A HREF="https://www.revolvermaps.com/?target=setup" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">RevolverMaps Standard Classic | RevolverMaps - Free 3D Visitor Maps</A>
                    <DT><A HREF="http://www.revolvermaps.com/?target=setupgl" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">RevolverMaps Standard GL | RevolverMaps - Free 3D Visitor Maps</A>
                    <DT><A HREF="http://fontawesome.io/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Font Awesome, the iconic font and CSS toolkit</A>
                    <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Mockup</H3>
                    <DL><p>
                        <DT><A HREF="http://www.layoutit.com/es/dashboard#.VQdwA-GefZ4" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">LayoutIt! - Interface Builder for Bootstrap</A>
                        <DT><A HREF="https://www.layoutit.com/es/dashboard#.VQdwA-GefZ4" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">LayoutIt! - Interface Builder for Bootstrap</A>
                    </DL><p>
                    <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971606">tools</H3>
                    <DL><p>
                        <DT><A HREF="http://www.colorzilla.com/gradient-editor/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Ultimate CSS Gradient Generator - ColorZilla.com</A>
                        <DT><A HREF="http://960.gs/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">960 Grid System</A>
                        <DT><A HREF="http://es.lipsum.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:http://es.lipsum.com/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABvElEQVQ4jZWSsWtaURjFf999+tSmDg9JhyJIQCFkciikKIiTdGz7UCQugZBBSoZu2frGDv0Xupf8HV1LSTdHEZyegUIbmjx9p4OWVpraeODC5fKdH/fce2ClyWRSkLQraQdAUl7SI0kP2aAM4IC00+mcVSqV8/F4fAl8rlarB/v7+3XP8z5Iem1m2gQCKHW73Rd7e3uxmanRaHyp1+tt4PH/jGsql8tvgiC4jaLo2X3m3R97D3Bpmv4oFAqZq6urBHBRFLl/eP8CCEh933eSLJvNOiCNoujeNzCANE3XBrYBLA+cw8w2mjYCttWdAEnM53NguwiC5RuYGb7v2wq2ViBJJilzF8AA55xjsVgojuMbwPV6vSxg7XY7A3gnJydPj4+P30vKwrLKv7QAyOfzN3EcazabHUj6aGa3kszM5gCj0WiQy+We3BV/t9/vN2q12iWgIAi+Hh4evjs9PT0D6mEYPm+1Wm9LpZLCMByuPJ6tSGmz2Tx3zr2SlDrnFkmSeL7v7xSLRV1fX888z3swnU53giD4NhwOXw4Gg0/A7w+/uLgoJEmSPzo6cixrDZCuomWAZLWywHczSwB+AjEmqNuXtcxVAAAAAElFTkSuQmCC">Lorem Ipsum - All the facts - Lipsum generator</A>
                        <DT><A HREF="http://es.lipsum.com/feed/html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Lorem Ipsum - All the facts - Lipsum generator</A>
                        <DT><A HREF="https://regex101.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Online regex tester and debugger: JavaScript, Python, PHP, and PCRE</A>
                        <DT><A HREF="http://www.javascriptobfuscator.com/dashboard/home.aspx" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Javascript Obfuscator Dashboard</A>
                        <DT><A HREF="http://codebeautify.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Free Online Tools For Developers - To Beautify, Validate, Minify, Analyse and Convert your JSON, XML, JavaScript, CSS, HTML, Excel</A>
                        <DT><A HREF="http://www.tablesgenerator.com/html_tables" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">HTML Table generator - TablesGenerator.com</A>
                        <DT><A HREF="https://www.colorzilla.com/gradient-editor/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Ultimate CSS Gradient Generator - ColorZilla.com</A>
                        <DT><A HREF="https://es.lipsum.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Lorem Ipsum - All the facts - Lipsum generator</A>
                        <DT><A HREF="https://es.lipsum.com/feed/html" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Lorem Ipsum - All the facts - Lipsum generator</A>
                        <DT><A HREF="https://www.javascriptobfuscator.com/signin.aspx" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Javascript Obfuscator Dashboard</A>
                        <DT><A HREF="https://codebeautify.org/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Free Online Tools For Developers - To Beautify, Validate, Minify, Analyse and Convert your JSON, XML, JavaScript, CSS, HTML, Excel</A>
                        <DT><A HREF="https://www.tablesgenerator.com/html_tables" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">HTML Table generator - TablesGenerator.com</A>
                    </DL><p>
                    <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Iconos y Fuentes</H3>
                    <DL><p>
                        <DT><A HREF="http://www.fontsquirrel.com/fonts/list/find_fonts?q%5Bterm%5D=quadro&q%5Bsearch_check%5D=Y" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Find Free Fonts | Font Squirrel</A>
                        <DT><A HREF="http://www.fontsquirrel.com/fonts/quattrocento-sans" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Free Font Quattrocento Sans by Impallari Type | Font Squirrel</A>
                        <DT><A HREF="http://openphoto.net/gallery/name/computers/47" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Technology / Computers | openphoto.net (BETA)</A>
                        <DT><A HREF="http://www.1001freefonts.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">1001 Free Fonts - Download Free Fonts</A>
                        <DT><A HREF="http://all-free-download.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Free Vector graphic art, free photos, free icons, free website templates, psd graphic, photoshop brush, font, free download</A>
                        <DT><A HREF="https://www.facebook.com/?sk=h_chr" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Facebook</A>
                        <DT><A HREF="http://techtastico.com/post/coleccion-iconos/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Super colección de iconos gratis +7500</A>
                        <DT><A HREF="https://www.fontspring.com/free/300" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Families with Free Fonts | Fontspring</A>
                        <DT><A HREF="https://fonts.google.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Google Fonts</A>
                        <DT><A HREF="https://www.iconspedia.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Icons &amp; Icon Packs - Download Free PNG Icons | IconsPedia</A>
                        <DT><A HREF="https://dummyimage.com/#standards" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Dynamic Dummy Image Generator - DummyImage.com</A>
                        <DT><A HREF="https://www.fontsquirrel.com/home" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Handpicked free fonts for graphic designers with commercial-use licenses. | Font Squirrel</A>
                        <DT><A HREF="https://www.iconspedia.com/signup.php" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Icons &amp; Icon Packs - Download Free PNG Icons | IconsPedia</A>
                        <DT><A HREF="https://www.fontsquirrel.com/fonts/list/find_fonts?q%5Bterm%5D=quadro&q%5Bsearch_check%5D=Y" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Find Free Fonts | Font Squirrel</A>
                        <DT><A HREF="https://www.fontsquirrel.com/fonts/quattrocento-sans" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Free Font Quattrocento Sans by Impallari Type | Font Squirrel</A>
                        <DT><A HREF="https://openphoto.net/gallery/name/computers/47" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Technology / Computers | openphoto.net (BETA)</A>
                        <DT><A HREF="https://www.1001freefonts.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">1001 Free Fonts - Download Free Fonts</A>
                        <DT><A HREF="https://all-free-download.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Free Vector graphic art, free photos, free icons, free website templates, psd graphic, photoshop brush, font, free download</A>
                        <DT><A HREF="https://fonts2u.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Fonts2u.com free fonts</A>
                        <DT><A HREF="https://www.stockvault.net/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Free Stock Photos | Stockvault.net - Free Photos - Free Images</A>
                        <DT><A HREF="https://techtastico.com/post/coleccion-iconos/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Super colección de iconos gratis +7500</A>
                        <DT><A HREF="https://www.fontsquirrel.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">Handpicked free fonts for graphic designers with commercial-use licenses. | Font Squirrel</A>
                    </DL><p>
                    <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">git</H3>
                    <DL><p>
                        <DT><A HREF="https://git-scm.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Git</A>
                        <DT><A HREF="https://help.github.com/categories/repositories/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Repositories - User Documentation</A>
                        <DT><A HREF="http://rogerdudler.github.io/git-guide/index.es.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">git - la guía sencilla</A>
                        <DT><A HREF="https://packagist.org/packages/niklasravnsborg/laravel-pdf" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://packagist.org/packages/niklasravnsborg/laravel-pdf" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAC90lEQVQ4jXWSXUxTdxjGfz3ntKdAP+jAj26LsVBEKdOUSEOnq8BcYJ+ZRi/mjSYubFyoIZkXS5aZbBdmW8KWuKtl2UeCWyYsumAiwkW3jLp2TEkwynBwisRNmBEoreW05Zz/bk1Xnqs3b37P+z4XD6yjmrqGt7/4qj/74dlz92TZ9vp6nPzYvKmuPtDT2Bg8WllVtaf3sy8/eL5jv7ozGHIFm0KHDMPYmVpKZz3VVbtXlpceAhkAC4Ddbm87dvzkd7uCuzerqp1nAo3Mzc0SDO0hp68yc2cKX81WRoavki/kuTTQN3It9vOLgKEANDWHO3tOv7c5nU4TvXqJ5JNVLOqPKOR0PB432YLO+NQEimWNcFsHblflCwaFcCIWG1UAnA6nunGjk6nJWyxlMpx+/1Nc2Xl6T+jYVJUzn5wlWfE0bzbX0rr/NcJ7W7nY/80GAAVAVqxPZDIGpmnS2vYSt29OENl7lJbn2hFCcKijk5mkxssdB7h+I0H42VYcDmclgByNRqslxflRQ2CXS9P+Ij4aJdjUTCgcobzCgdvjIRLZhyQpOMorkCSJrbV+VlKLa8NDgxckVVWrt9UHnvJ6VfL6Kh6HBV/NNnx+H7IsM6dp5PKC/GqKocvf43S6KS8DX41/uxDCorjdbu3Eqa53R0bCbTu272iqq6+vVhQrwgSr1UpydoYf+/sQIk/nK4cBQfy36yTisWsHX20X/+tPV/fJB1+fHxQ3bv4t5hYMMamlxMXLMRH7QxOjY9Oiq/udAZut7LDf71dLNisUipwZ+OkXMTiUEP8sCTG7YIj7i0L8+vu0OP5Wz5/FvFS8GB8fG7JabZimgXZnhmwmzVgijqIo3L93d7SYt5RKsWGT99T5C8Mfy7LFtvDvPB6Xh+V06uEbB9pbgOmS0Ytk39fScndiakH0nvtW9P1wRTRs8d4q9VBZ50BASsa3fH6kljWLFYuxSn5eLwBlQPZxUC7tp/Agx7JXyTfaTF1febSWS6ToNk0mi8H/AF4NLR1yVBzmAAAAAElFTkSuQmCC">niklasravnsborg/laravel-pdf - Packagist</A>
                        <DT><A HREF="https://mpdf.github.io/getting-started/creating-your-first-file.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Creating your first file – Getting Started – mPDF Manual</A>
                        <DT><A HREF="https://binaryhash.wordpress.com/2015/08/17/install-pdftk-server-on-mac-using-home-brew/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Install pdftk server on mac using home brew – Shyam Mohan</A>
                        <DT><A HREF="https://github.com/spl/homebrew-pdftk" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">GitHub - spl/homebrew-pdftk: Homebrew Formula for PDFtk Server (UNMAINTAINED)</A>
                    </DL><p>
                    <DT><A HREF="https://viewdns.info/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">ViewDNS.info - Your one source for DNS related tools!</A>
                    <DT><A HREF="https://placeholder.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Placehold.it - Quick and simple image placeholders</A>
                    <DT><A HREF="https://mdbootstrap.com/docs/standard/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Material Design for Bootstrap 4 or 3</A>
                    <DT><A HREF="https://www.layoutit.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">LayoutIt! - Interface Builder for Bootstrap</A>
                    <DT><A HREF="https://mailtrap.io/signin" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">User Profile - Mailtrap</A>
                    <DT><A HREF="https://www.revolvermaps.com/?target=setupgl" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">RevolverMaps Standard GL | RevolverMaps - Free 3D Visitor Maps</A>
                    <DT><A HREF="https://gratisography.com/#0" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Gratisography: Free, use as you please, high-resolution pictures.</A>
                    <DT><A HREF="https://fontawesome.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Font Awesome, the iconic font and CSS toolkit</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971903">Responsive</H3>
                <DL><p>
                    <DT><A HREF="http://getuikit.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">UIkit</A>
                    <DT><A HREF="http://materializecss.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Documentation - Materialize</A>
                    <DT><A HREF="http://responsive.gs/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Responsive Grid System</A>
                    <DT><A HREF="http://foundation.zurb.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Foundation | The Most Advanced Responsive Front-end Framework from ZURB</A>
                    <DT><A HREF="https://html5boilerplate.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">HTML5 Boilerplate: The web’s most popular front-end template</A>
                    <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971903">Visual Studio</H3>
                    <DL><p>
                        <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971903">Massive</H3>
                        <DL><p>
                            <DT><A HREF="https://github.com/alexandernyquist/massive-mysql/blob/master/README.markdown" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">massive-mysql/README.markdown at master · alexandernyquist/massive-mysql · GitHub</A>
                            <DT><A HREF="https://github.com/pinscript/massive-mysql/blob/master/README.markdown" ADD_DATE="1667664395" LAST_MODIFIED="1725971903">massive-mysql/README.markdown at master · alexandernyquist/massive-mysql · GitHub</A>
                        </DL><p>
                        <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971455">Simple Dara</H3>
                        <DL><p>
                        </DL><p>
                        <DT><A HREF="http://community.sharpdevelop.net/forums/p/14123/48584.aspx" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">SharpDevelop Reports, una solución o un problema para bases de datos MySQL y PostgreSQL. - SharpDevelop Community</A>
                        <DT><A HREF="https://github.com/alexandernyquist/massive-mysql" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">alexandernyquist/massive-mysql</A>
                        <DT><A HREF="https://github.com/pinscript/massive-mysql" ADD_DATE="1667664395" LAST_MODIFIED="1725971606">alexandernyquist/massive-mysql</A>
                    </DL><p>
                    <DT><A HREF="https://getuikit.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">UIkit</A>
                    <DT><A HREF="https://materializecss.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Documentation - Materialize</A>
                    <DT><A HREF="https://www.bigdropinc.com/blog/responsive-gs/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Responsive Grid System</A>
                    <DT><A HREF="https://get.foundation/" ADD_DATE="1667664395" LAST_MODIFIED="1725971174">Foundation | The Most Advanced Responsive Front-end Framework from ZURB</A>
                </DL><p>
                <DT><A HREF="https://scotch.io/tutorials/reorder-css-columns-using-bootstrap" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Reorder CSS Columns Using Bootstrap ♥ Scotch</A>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">bootstrap</H3>
                <DL><p>
                    <DT><A HREF="https://bootsnipp.com/tags/login?page=3" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bootstrap Login Examples</A>
                </DL><p>
                <DT><A HREF="https://mdbootstrap.com/education/bootstrap/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bootstrap 4 tutorial - best &amp; free guide of responsive web design - Material Design for Bootstrap</A>
                <DT><A HREF="https://www.cssportal.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CSS Portal - Templates, Tutorials, Books, Software, Code Examples - CSS Portal</A>
                <DT><A HREF="https://css-tricks.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CSS-Tricks - Tips, Tricks, and Techniques on using Cascading Style Sheets.</A>
                <DT><A HREF="https://960.gs/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">960 Grid System</A>
                <DT><A HREF="https://bootsnipp.com/snippets/3k59p" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Bootstrap Snippet Custom Search input using HTML CSS Bootstrap | Bootsnipp.com</A>
                <DT><A HREF="https://www.anieto2k.com/2006/03/23/efectos-css-increibles/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Efectos CSS increibles | aNieto2K</A>
                <DT><A HREF="https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css/" ADD_DATE="1667664395" LAST_MODIFIED="1725970839" ICON_URI="fake-favicon-uri:https://lenguajecss.com/css/maquetacion-y-colocacion/grid-css/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAADBUlEQVQ4jV2Sy4tbdRTHP7/ffeXm5ubRScaM80otaacjOlYrKAUfTItaaBeCi67UjQvBbgQ3LnQx4MKuKgX/APeCFRFKtdCFMA6jjNDRMrZaMs3jJpMmk2SS+/q5CDNt/a7OOZzz5fs954jFz6592R6EH/lhrKQQAf9DHEaPFxTEAtO2jDBt61/rL87ndm5utf1h4LsjP0r0egFoApQCKTm0NA9inAexouhaqN0BYcXbO5ZPdPXDheT22r1O459W6C5MJpk5kmEYxKhYITXJ/NIUQgiUUiQ0QS0SrG1sk4JmueBU9axj1LO20YibgyPLr85y+cIJYPiI5sRjDlY2HvBdrctLKbM2dcip6rZueClL87B1frvX5eraHbxeQBTHCCkolqbZDWJeKNgczZo0RxH4IZmMXk0nZVXPm3oj55g1bJ2Nyi7nL/8+9uz1QdfgdR9aI6688xRHsxO0hmOCnJOsZ+ykp9sT095kun0fP8J0LZysRd4x+Pz9RQIFk6UpukHM8rQDwM4whCCk4Fr1jCFb+tmyGH367WYVQArojyI0IXjvtRIgAePhSRXsDEIIIzJJs/7GUrGvA6STsoEUADyZtfD9mFe++IWEpVF89jDdIOab0zNYmqQzDAFFzjWrADpAPmXVEYJmL+DGxeeYTBksfHAdHAOMHIwiUm/N0RxFDPwQlKKYsR4SOJZsmKaG3w+wkybH5vJ8/O5xfvjrAXPzKd4suQDcH0R0BwGmBq5ueAcEdspuOJaOPwi5udnkZMnl0oXnuaSG4z8QY3u3Oz6BH2JLgWXIFoDYX9DMJz/2Onuho4DFYpKXS2nefiZPYXaK7+92WfWG3AkkA69De32rV//qvHugACAaha3dVt+RboLVrQ6rfzS5cqPCzBlF148x/QDd96nc2mY6Vo39ObkffHi6vHJqqbhWcM0IYpBgmBrDSpP2+t/Uf73N6Na/4cmcsXrx3PGV/bkDC/v4+W47u77lLf9Z6535abN5LtwL4lPl7NUTs7lrTy88cf1seaL7aP9/78xBFa4JLPsAAAAASUVORK5CYII=">Grid CSS (Cuadrículas) | CSS en español</A>
                <DT><A HREF="https://www.digitalocean.com/community/tutorials/reorder-css-columns-using-bootstrap" ADD_DATE="1667664395" LAST_MODIFIED="1725970839">Reorder CSS Columns Using Bootstrap ♥ Scotch</A>
                <DT><A HREF="https://mdbootstrap.com/docs/standard/bootstrap-5-tutorial/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Bootstrap 4 tutorial - best &amp; free guide of responsive web design - Material Design for Bootstrap</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725970842">data</H3>
            <DL><p>
                <DT><A HREF="https://www.google.es/search?client=ubuntu&channel=fs&q=base+de+datos+coches&ie=utf-8&oe=utf-8&gfe_rd=cr&ei=Qiw-Vea9NcKp8weB6oGYDg#channel=fs&q=base+de+datos+venta+de+autos&revid=785737761" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">base de datos venta de autos - Buscar con Google</A>
                <DT><A HREF="http://www.codigospostales.com/38" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Códigos Postales de Santa Cruz de Tenerife</A>
                <DT><A HREF="http://www.solosequenosenada.com/2010/09/16/listado-de-todos-los-codigos-postales-de-espana/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Listado de todos los códigos postales de España | Solosequenosenada</A>
                <DT><A HREF="https://github.com/alombarte/utilities/tree/master/sql" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Municipios y Provincias España</A>
                <DT><A HREF="http://www.harecoded.com/volcado-mysql-municipios-provincias-espanolas-territorios-ue-1963492" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Volcado Mysql de municipios y provincias españolas y territorios UE</A>
                <DT><A HREF="https://www.codigospostales.com/38" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Códigos Postales de Santa Cruz de Tenerife</A>
                <DT><A HREF="https://www.solosequenosenada.com/2010/09/16/listado-de-todos-los-codigos-postales-de-espana/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Listado de todos los códigos postales de España | Solosequenosenada</A>
                <DT><A HREF="https://www.harecoded.com/volcado-mysql-municipios-provincias-espanolas-territorios-ue-1963492/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Volcado Mysql de municipios y provincias españolas y territorios UE</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Diseños</H3>
            <DL><p>
                <DT><A HREF="http://perfecticons.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Perfect Icons - A social icon creation tool.</A>
                <DT><A HREF="https://pixabay.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://pixabay.com/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAACbElEQVQ4jZWSv0tbURzFv9/7bvKe+fEMJSYYQiqFWCuo1A4dWnEQqRBpG+rgIIrg4uCQwUHBv0AySEZFBSF27qDFOgiC1g5ih6KoVCQNUUxqX6J5ebnv3tsh0kLBoWc65yxnOB/sf98P/yMipZRSggQp5Z/2H/83SiCIiIgSpUIUAOCCA4BCFC64LWwEBABEFFIwwSTIuwUCpGSVGGca1SzbKlkln+bTnXqVVwkSW9iqovrr/IioNA80I2KZlXsf9c50zYx0jHQ/7M4UM16nN/UqlTfz+xf7AVcg1ZcKuoNb51tEQeW2etvT1DP1Yury5nLxYLHCKsnepMnM7cx24nki6AqOPxv3u/zLX5cpoRhbjTHOVt6snP06S3xKUEIJkvnYvMWtyc3JpddLtrAbPY3Jz8m107V6rZ5wwXVVb3A37GZ3NaqFvCEhxc6PneiDqGEZ66frYT2cMTIb3ze8qpcLTiRKQAAAJlipWiqYBcZZe6D93DgP6+GBJwNH+aOILzLYOmhUDIUoSvRdVFXU+ON4vpxHxKb6puGO4a5I19yXubGnYz7NN/ph1OP0DLUP7WX3cjc5CgAEicnMeEs83hIHAJOZszuzET3S2diZ2EjY0l44WGgLtE2/nJ74OIF96T6v05t+m05/S2+ebXqcnoubi+vKdau/1bTNbDGrObQqr7od7pAnlLvJ0drtVKFX5avjwrFP8yGiruonP08QUaUqF9xBHKZtHhYOnYqTIqKUslgpAoDL4dKoZkubC65RDQCEFDUuCJI6WidBYmw1hohuh9uyLSZYjTFEvI/WuwXDMggSgkSCrAF3n34Dy0gtnato010AAAAASUVORK5CYII=">Imágenes gratis - Pixabay</A>
                <DT><A HREF="https://www.behance.net/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Portafolios online en Behance</A>
                <DT><A HREF="http://www.yelp.com/madrid" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Madrid Restaurants, Dentists, Bars, Beauty Salons, Doctors</A>
                <DT><A HREF="http://www.yelp.com/styleguide" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Styleguide</A>
                <DT><A HREF="https://emojiguide.com/blog/smile-emoji-list/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Perfect Icons - A social icon creation tool.</A>
                <DT><A HREF="https://www.yelp.es/madrid" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Madrid Restaurants, Dentists, Bars, Beauty Salons, Doctors</A>
                <DT><A HREF="https://www.yelp.com/styleguide" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Styleguide</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971452">fuentes</H3>
            <DL><p>
                <DT><A HREF="https://www.typetester.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Typetester – Compare and test Web fonts from Adobe Edge, Google and Typekit web hosting services</A>
                <DT><A HREF="http://fontello.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Fontello - icon fonts generator</A>
                <DT><A HREF="https://fontello.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Fontello - icon fonts generator</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971439">Hosting</H3>
            <DL><p>
                <DT><A HREF="http://www.banahosting.com/es/hosting-revendedores.shtml" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Hosting Revendedores - Planes Reseller - BanaHosting</A>
                <DT><A HREF="https://www.banahosting.com/es/hosting-revendedores.shtml" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Hosting Revendedores - Planes Reseller - BanaHosting</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971452">Javascript &amp; JQuery</H3>
            <DL><p>
                <DT><A HREF="http://www.slidesjs.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">SlidesJS, a responsive slideshow plug-in for jQuery (1.7.1+) with features like touch and CSS3</A>
                <DT><A HREF="http://www.jsdelivr.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">jsDelivr - Free open source CDN for javascript libraries, jQuery plugins, CSS frameworks, Fonts and more</A>
                <DT><A HREF="http://www.codeofaninja.com/2013/05/crud-with-php-jquery.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CRUD with jQuery And PHP - Step By Step Guide</A>
                <DT><A HREF="https://www.datatables.net/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">DataTables | Table plug-in for jQuery</A>
                <DT><A HREF="http://jeasyui.com/documentation/index.php#" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Documentation - jQuery EasyUI</A>
                <DT><A HREF="https://oscarotero.com/jquery/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">jQuery Cheat Sheet</A>
                <DT><A HREF="https://phpsblog.wordpress.com/2009/12/17/anadiendo-ajax-en-codeigniter-con-jquery/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Añadiendo AJAX en CodeIgniter con jQuery | Php&#39;s Blog</A>
                <DT><A HREF="http://www.jeasyui.com/download/index.php" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Download jQuery EasyUI 1.4.3 - jQuery EasyUI</A>
                <DT><A HREF="http://techtastico.com/post/cuales-son-las-mejores-librerias-javascript-para-desarrollo-web/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">¿Cuales son las mejores librerías Javascript para desarrollo web?</A>
                <DT><A HREF="http://techtastico.com/post/31-trozos-de-codigo-de-jquery-que-te-haran-ser-un-profesional-en-javascript/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">31 trozos de código de jQuery que te harán ser un profesional en JavaScript</A>
                <DT><A HREF="http://albertoromeu.com/90-recursos-javascript-y-css3-para-mejorar-la-ux-de-tus-webapps/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">90 recursos Javascript y CSS3 para mejorar la UX de tus webapps - Protips</A>
                <DT><A HREF="https://www.jsdelivr.com/?query=semantic" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">jsDelivr - A free super-fast CDN for developers and webmasters</A>
                <DT><A HREF="http://jsfiddle.net/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:http://jsfiddle.net/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACi0lEQVQ4jY2TTUhUYRSG3/PdO3d+nL8mdcYxpDYV5iaCaleQLYIWQozYRmjhIolqpsxMokv0I5UzIYIQlIEJZQQFRhAtDGtRUG3btCruDOSMM/dajnPnfqeFjQqB+a4+zsdzeDnnPYT1pLMAINAKBgB0QgLE6zL/1XLTFalr3oTElAASwFNyACCWKR0REvtY0zRh23lmdco4R98BppoTWmZXCwCwaagQ8rpdYwy2CXgLoeQheQfAhxn0MJv0T9YYqkGBO2Z9HckEgSyQ6CBHzhh9odG1dqO3rUZFxaSs2ndzfZGXgC5o+aO4TVGVMQJmwdzCJOaNpP8iEqwsW/okEN9D0KlSP2xu1wjDhhk4Bp1sAEBzxrocS1u9G51jc9qcCN9c3LoyRCbezVU5CgCxtHVA1dzdbC+ZC2XnamkgPN80bKaUgK/V+bX4MZsM3JNEcz539UQRuEJNafMSEcWNkj8V8RYaPZr6QEK7IajaBuZD0pGTQoi9rHkeC3tpUHL10W8PzfjK4j4gXwsCtRsV/wB0qrhd7jZAfM0lvTPG2cCow/hAiug3UsEL2VPaZ4edJ0TK/lJveN4UgZMEpZPiaXPaSAWPQtdFOHQm6GNlQkC8cQTvRBVfWLAtwF2AeAGSHTaJaz+L/nfQScbT5jTFM+ZsuWIfL/Rv/gEADbcWYpqLe6TkXNYKjEOnajRTbFeF6yBL55WRDL4HgLrrC9GQTz6jaLrUpRJ1s+IZLBesbwXkytB3VQBgS5q9ZXtOnetvsGobiIzkgy7WWhRHDknGFK1EVrh6wA5YwiFiFQCI4YCImVkBgZjJIbCAUBRUnXHjfPA5rY1xZCQf/H8KIiicJnP1BIB/LmxD+sv8AWPVHepeoPYgAAAAAElFTkSuQmCC">Create a new fiddle - JSFiddle</A>
                <DT><A HREF="http://jsbeautifier.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:http://jsbeautifier.org/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAxElEQVQ4ja2SsQ2DMBREHygNQmIEKgawR8gmUDIDBaJgACQELZPACCxAgSiYgY5UQcI2IYT87j+dz6ez4V8ThuH6i86+a/K4kqZpGktlG/j2dtXMmMB1Xcqy3LE4jlmWRdPaKvA8TzsMUNc1juOcGxRFQSsEnZQb66SkFYKqqs4NACxL68rI4KCDZ99/3E8TXBnNIMuyQ3GSJMcG73cdx5E8zzVhmqbM87zTgtKB7/tM08QwDERRZEwRBMFuN1Z75Svfnhet20BRufj1bQAAAABJRU5ErkJggg==">Online JavaScript beautifier</A>
                <DT><A HREF="http://techtastico.com/post/jquery-una-buena-alternativa-para-prototype-o-mootools/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">jQuery una buena alternativa para Prototype o Mootools</A>
                <DT><A HREF="http://www.noupe.com/tutorial/drop-down-menu-jquery-css.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Sexy Drop Down Menu w/ jQuery &amp; CSS - Noupe</A>
                <DT><A HREF="http://techtastico.com/post/como-crear-codigo-javascript-sin-saber-programar-javascript/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Cómo crear código JavaScript sin saber programar JavaScript</A>
                <DT><A HREF="https://storybook.js.org/tutorials/intro-to-storybook/vue/en/simple-component/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Build a simple component | Storybook Tutorials</A>
                <DT><A HREF="https://nuxtjs.org/showcases#E-Commerce" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Nuxt - Showcases</A>
                <DT><A HREF="https://slidesjs.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">SlidesJS, a responsive slideshow plug-in for jQuery (1.7.1+) with features like touch and CSS3</A>
                <DT><A HREF="https://www.jsdelivr.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">jsDelivr - Free open source CDN for javascript libraries, jQuery plugins, CSS frameworks, Fonts and more</A>
                <DT><A HREF="https://codeofaninja.com/javascript-crud-tutorial/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">CRUD with jQuery And PHP - Step By Step Guide</A>
                <DT><A HREF="https://techtastico.com/post/cuales-son-las-mejores-librerias-javascript-para-desarrollo-web/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">¿Cuales son las mejores librerías Javascript para desarrollo web?</A>
                <DT><A HREF="https://techtastico.com/post/31-trozos-de-codigo-de-jquery-que-te-haran-ser-un-profesional-en-javascript/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">31 trozos de código de jQuery que te harán ser un profesional en JavaScript</A>
                <DT><A HREF="https://jsfiddle.net/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Create a new fiddle - JSFiddle</A>
                <DT><A HREF="https://beautifier.io/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Online JavaScript beautifier</A>
                <DT><A HREF="https://techtastico.com/post/jquery-una-buena-alternativa-para-prototype-o-mootools/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">jQuery una buena alternativa para Prototype o Mootools</A>
                <DT><A HREF="https://www.noupe.com/inspiration/tutorials-inspiration/drop-down-menu-jquery-css.html" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Sexy Drop Down Menu w/ jQuery &amp; CSS - Noupe</A>
                <DT><A HREF="https://techtastico.com/post/como-crear-codigo-javascript-sin-saber-programar-javascript/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Cómo crear código JavaScript sin saber programar JavaScript</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Markdown</H3>
            <DL><p>
                <DT><A HREF="https://readthedocs.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Inicio | Read the Docs</A>
                <DT><A HREF="https://www.gitbook.com/book/wcervini/massive/edit#/edit/master/SUMMARY.md" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">SUMMARY.md (master) - GitBook Editor</A>
                <DT><A HREF="resource://markdown_here_common/options.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Markdown Here Options</A>
                <DT><A HREF="https://www.gitbook.com/?utm_source=legacy&utm_medium=redirect&utm_campaign=close_legacy#/edit/master/SUMMARY.md" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">SUMMARY.md (master) - GitBook Editor</A>
            </DL><p>
            <DT><A HREF="https://manuals.setasign.com/fpdi-manual/the-fpdi-class/examples/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Examples</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971452">SEO</H3>
            <DL><p>
                <DT><A HREF="https://gtmetrix.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">GTmetrix | Website Speed and Performance Optimization</A>
                <DT><A HREF="https://hootsuite.com/es/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Su plataforma para interactuar, escuchar y compartir en redes sociales | Hootsuite</A>
                <DT><A HREF="http://www.bing.com/toolbox/webmaster" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bing - Herramientas para administradores de web</A>
                <DT><A HREF="http://keywordtool.io/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Keyword Tool: FREE Alternative to Google Keyword Planner</A>
                <DT><A HREF="https://www.google.com/trends/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Tendencias de búsqueda de Google</A>
                <DT><A HREF="https://developer.chrome.com/devtools" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://developer.chrome.com/devtools" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACMElEQVQ4jaWTS0iUURTHf+d+M85oOb4SQ6OFYAbRgxbRpkUPKYwUsSDoSVDroEVtaykE1aKoFpERBLqIQIsWBomCjRYRQZTRJtQWSSYz+Zjv/lt8nw+QatGBwz333vO65/+/SKqQ1CXJSwrj9U+y3KdLUgWxIUmFfwQvT1KI7S6TJMADFqsUFgzAXICAUB6AhAu04BOrMym+lQxJOGf8RbwkMzOLEmCSvPcyzOQMEzDT8xiAdHMrAPc/9mHAqQ17wAwvCWTOnMx7L7Ooq5mRYXKddygMDVCY/UXdo2cM1aTZ2XkOS6ZoWreNS9sPs7tuy0I3OBBjY9O8udbJ3PmT2GAfoTlKmg6i2lrqS6pobdiFmXj+9S0tvVc48+I6X35+i4aWn/U6fXOa8Yk8e3MDHJ3uofH4IdjXRggsjO3B5ywd2bu8n86j+RwN5WsZbr9KInCQWZ3gU1EZveVtvE43c6SymPY5UVwkvDko5DiR6qe55ik3EpXc/l5FY2YTySDA5L2m8uLh4DxPhmeZzBvyns3rAzqOraIqNc589gDhj3ekHVgqyUTNBaobLhIky4iHGEE0OuG593KO/g8hgfPcOltKY+kIcwM7cADVLVj9ZRKZrTHyPoJRkgmTMxkYr0YLZEqMjbUOYWgqC/OTuDX7I/AVCpyZmZaIBCYQEU/iCmAIFvfClg4WibSCymH8KlvkZFTDbCWVHdANuNhLgAXOcM4wW9AAs4BlwT6O6eZ/v/Nvwwmu1r04AVkAAAAASUVORK5CYII=">Chrome DevTools Overview - Google Chrome</A>
                <DT><A HREF="http://archive.org/web/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Internet Archive: Wayback Machine</A>
                <DT><A HREF="https://www.google.com/webmasters/tools/home?hl=es" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Search Console - Página principal</A>
                <DT><A HREF="https://moz.com/tools" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Free SEO Tools &amp; Moz Pro Software - Moz</A>
                <DT><A HREF="http://adwords.google.com/keywordplanner" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Google AdWords: Keyword Planner</A>
                <DT><A HREF="https://developers.google.com/speed/pagespeed/insights/?url=www.martinmotors.es" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">PageSpeed Insights</A>
                <DT><A HREF="http://www.quicksprout.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Quick Sprout — I&#39;m Kind of a Big Deal</A>
                <DT><A HREF="https://serps.com/tools/rank_checker" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Keyword Rank Checker &amp; SERP Checker Tool for Google, Yahoo Positions</A>
                <DT><A HREF="http://seositecheckup.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">SEO Tools, Software and Articles - SEO Site Checkup | SeoSiteCheckup.com</A>
                <DT><A HREF="http://seositecheckup.com/seo-audit/www.martinmotors.es" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Search Engine Optimization (SEO) Tools | SeoSiteCheckup.com</A>
                <DT><A HREF="http://suite.searchmetrics.com/de/research" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Searchmetrics - SEO, Social, Keywords, Backlinks und Rankings</A>
                <DT><A HREF="http://www.vivirdelared.com/curso-de-seo-posicionamiento-web-paso-a-paso/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Curso de SEO – Posicionamiento Web Paso a Paso</A>
                <DT><A HREF="https://www.hootsuite.com/es" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Su plataforma para interactuar, escuchar y compartir en redes sociales | Hootsuite</A>
                <DT><A HREF="https://www.bing.com/webmasters/about" ADD_DATE="1667664395" LAST_MODIFIED="1725970842" ICON_URI="fake-favicon-uri:https://www.bing.com/webmasters/about" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACXklEQVQ4jZWTT0hUURjFz3ffn3FGZ9RMTamFBS00KIgiKAIhCIqCiBGCCIKoXbtatchq61JI2gS1GmmR4MrAIGghriKpaJOZ6YzMvHHmvZl377vvfi1egxoV9e0ul/Pju+ecCwAAMwHAiXn/zKk34U38xwgAwDgIAIQW15yO1NTJuebs8dnawX8H3AcDAEtS2oOx3LZzFpwXR6fY+VcAAQCUII5AUVnGrMSQvQ/p5J5F65m/B/wcEwEsQaxgsYTWK9AJgAyIGAW2fgXYO04hCARAEgBiD55z7BUXWJiKIvno3Sh9+/sGIYElwFKAQxJBrVuDeI/dJ24Zx1oYWgjuYWnJ/SOAA4bxGSYw4CZbxTsURLZ5LBtgTbo36sk87Ned08OFLUjLxGSDIILxAeNrmHoc781zeq3LeimbzZLqzdhhsxT1dLVf7B5x8wCAQsFKAJzEaOoG8SbB1GOYumZ3v+cWD6MRdcSjflyfcCrK2+XA5FJ0GgCQz3NiYmIdaz82SBk2UoMJVC/pGCDun15e72RLllZVh3ekiv7LKtGNb6XAAKB9mTahBLOmWBqz8Ql8dqZ6Qxb5gbOZGWj3ypH8aAmzHrwHAAxP044i5QZRiaoN+F/9yLYiXJjIzrlu+xNLYIBUXWa6dzspJ14OV9RzAMDYWJy0i5lAxFc+80h50V/UfiyyB9qMSFltsugrVRWurmXhr27OBI3m7Q+Tg8utFLbq2YJ856sUYTJuIKdrgPIMwrXgS7CB8bd3c0+36XgnYBvk/Lw8lMral0yItCoHXqMSPnt9vW8daP0H4pbkB1H4QbCB//9FAAAAAElFTkSuQmCC">Bing - Herramientas para administradores de web</A>
                <DT><A HREF="https://keywordtool.io/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Keyword Tool: FREE Alternative to Google Keyword Planner</A>
                <DT><A HREF="https://trends.google.com/trends/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Tendencias de búsqueda de Google</A>
                <DT><A HREF="https://developer.chrome.com/docs/devtools/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Chrome DevTools Overview - Google Chrome</A>
                <DT><A HREF="https://moz.com/free-seo-tools" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Free SEO Tools &amp; Moz Pro Software - Moz</A>
                <DT><A HREF="https://www.quicksprout.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Quick Sprout — I&#39;m Kind of a Big Deal</A>
                <DT><A HREF="https://seoscout.com/tools/schema-generator" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Schema Creator</A>
                <DT><A HREF="https://seositecheckup.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">SEO Tools, Software and Articles - SEO Site Checkup | SeoSiteCheckup.com</A>
                <DT><A HREF="https://seositecheckup.com/seo-audit/www.martinmotors.es" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Search Engine Optimization (SEO) Tools | SeoSiteCheckup.com</A>
                <DT><A HREF="https://suite.searchmetrics.com/de/research" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Searchmetrics - SEO, Social, Keywords, Backlinks und Rankings</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971439">Tools</H3>
            <DL><p>
                <DT><A HREF="http://www.fontsquirrel.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Handpicked free fonts for graphic designers with commercial-use licenses. | Font Squirrel</A>
                <DT><A HREF="https://www.sitepoint.com/filling-pdf-forms-pdftk-php/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://www.sitepoint.com/filling-pdf-forms-pdftk-php/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACz0lEQVQ4jU2Tz0ucZxDHPzPP865Fl10FY9i1f4FHcdfYQ3PyqKXm0lzTgrgecuuxxosgSKgQfzTJxWNzyyGXYvFW6Luh9OBFSKOguyDU2JS479bd55keXMWBgbnMj+9nZoRbNjEx8ZVX/S6afRFjHBQRAAxQkX9U5DeL8eXvb9++vs6RnvtqtbousAAQYwQwVcXMMDMAUdXrgltpmj4Gug6gWqk8894vhBC6ZhZVVbrdLlmWEULAe3/dMJhZTLyfLJVKw41m842rjI/PqHNPQwhdQJ1z2mq1KBQK/LC0JP9+/CjHx8ckSQKggMQYg6pOlu/e/UPxvtaTiapKq9WiWCzy4/q6zMzMUKlWrdPpiHPuRkpvGhPnaipm1RgjIuJarRaDg4P89Py5jI+Ps7mxwcsXL6RYLFq73b5hALgep6pajEMiQqfT4c7ICDs7O4yNjbG2tsb29jY/v3rF6uqqAHZ5ecktkESzIbWr2ADxzlmSywnAxadP/Ndus7+/z5f377OxsSG5XE7aWWaqKtLLc6Pl8hKA917OP3yw3d1dmZqaYu7BA0SElZUVnPd8PTfH5L177O3tWZZl4pwzM7uiipnEGK1/YEBOT0/t20eP7ODggG8ePsQ5x8nJCQCjo6PW398vMUYTEUFEpFqpnJnZkJkhIjjnuLi4kJGREcuyTKanp3myvMzJ8TG1xUU7fP+egYEBeuDPFUhVFREJACEE8vm8NRsNmZ2dtSfLyxweHjI/P29/vXtHPp+ndwcAqVoIm7d3e13EJ4n9fXYmaZqyWKvZ0dERhUKBEIJdv4GFsCm9U9703i90Op2uiGBmDiDLMpIkwczo6+sjxhgAkiTx3W53K63Xaw6QRrP5S6lcHlaRSRFRMxOAXC6HquK9x8xEVVVENJptpfX6Y+CqExAbjcabz0ulP0UkDwxj9tnNn5shqucq8isxfp/W60+BCPA/ES5dz5b/R84AAAAASUVORK5CYII=">Filling out PDF Forms with PDFtk and PHP</A>
                <DT><A HREF="https://www.pdflabs.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">PDF Labs: Tools, Services and Code for PDF Users and Programmers</A>
                <DT><A HREF="http://codepen.io/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:http://codepen.io/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACTElEQVQ4jY2TMW/iQBCF36yNlDQkSnGUaJsUSFGCDBWhgdoNPVT8DeTkf9DwExA/ggonSFSuQIqE7honHdKu510RGyXKFbfdm52dHT29DyRHJN9IFiQ9SaqqOudYHeccVVVL6cveN5IjIfkbwC8ACkCKokAQBAAgLy8vAIB2uw0A/HJHAAbAH5RTC1VV772WGzBJEgZBwCAImCQJqwW891puU5CklI9FRCAistlsMJ1O+fHxIRcXFwCA0+mEq6srzudziaKo+hTGGBpVNcYYcc7JbDZDp9Nhs9mUNE3R7XbR7XaRpimazaZ0Oh3OZjN478UYI6pqoKq63++11+uptVZXq9XZvMFgwMFgcNar1YrWWn18fNT9fq+qqiDJxWJBAGy1WsyyjMfjkXEcs16vs16vM45jHo9HZlnGVqtFAFwsFiTJkCScc7i9vUWv18Pd3R2ur69hrcVmswEAjMdjPDw84P39HZPJBN57OOdAEiEAiAgAQFVRmnnW1anqVa3qMSKCWq2GLMuwXq+x2+2w3W7RaDQQRRGiKEKj0cB2u8Vut8N6vUaWZajVap9DVFUPh4P2+3211upyuTybNhwOORwOz3q5XNJaq/1+Xw+Hw6eJRVGc45okCUVE4zhmnuccj8ecTCbM85xxHNMYo0mSsIp5URQ/g5SmKabTKfM8l8vLS5DE6XTCzc0N5/O5tNvtb0E6R5mkOucqYPj09MQwDBmGIZ+fn7+CpSS/RfkHTMYYiIi8vr5CRHB/f4+SkX/C9BXn4j9wrvreSI7+AvzfT4EQnpIjAAAAAElFTkSuQmCC">CodePen - Front End Developer Playground &amp; Code Editor in the Browser</A>
                <DT><A HREF="http://www.iconspedia.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Icons &amp; Icon Packs - Download Free PNG Icons | IconsPedia</A>
                <DT><A HREF="http://placeimg.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">PlaceIMG | Easy FPO and Dummy Images for Any Project</A>
                <DT><A HREF="http://codehero.co/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:http://codehero.co/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABQUlEQVQ4jeXSvUsCcRzH8e91IiUNaW1R6X5taW0ZCEVU9AAO/Q9N/Q1tTm0tLTUkUteDGD1hFEUQiKXooZkp0lmWnnrn9ft5/r5NQatb0Gt+f7YPl7ML0I6Otuq/OYCCc5xmng25aJRK9Cmbswt5wUWSqVZF0W/u5Flv1jZUcLpJPGG8vWuhEyjOLyMio5RKKRKJ5hzD9W0/In7dRxCRPMSy1kEtdIqIiNg4D3fwA/0AwMqKtnekiUHObG4chuTJBf3iEgBYtdazutLlcevhKwBopjOg+NbxR+uz/NLnyAuj6u4BItJUurLmY5Tq17dqQETE2sYmqGIQEbXjs4Jr4tUzJ08vGaUPRGSE1Ld2SDSGv9CkZOJtVqZUmwmJJiS+19btXeRMJqZUAcAyM0Ue41pgH3i+c2yEs1hUv8j9x2t8AxvHx+EIRy6iAAAAAElFTkSuQmCC">La mejor fuente para aprender habilidades técnicas en español - CODEHERO</A>
                <DT><A HREF="http://www.iconspedia.com/signup.php" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Icons &amp; Icon Packs - Download Free PNG Icons | IconsPedia</A>
                <DT><A HREF="http://dummyimage.com/#standards" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Dynamic Dummy Image Generator - DummyImage.com</A>
                <DT><A HREF="http://www.fontsquirrel.com/home" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Handpicked free fonts for graphic designers with commercial-use licenses. | Font Squirrel</A>
                <DT><A HREF="http://www.fontspring.com/free/300" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Families with Free Fonts | Fontspring</A>
                <DT><A HREF="http://www.gratisography.com/#0" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Gratisography: Free, use as you please, high-resolution pictures.</A>
                <DT><A HREF="http://randomkeygen.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Random Key Generator</A>
                <DT><A HREF="https://jsonplaceholder.typicode.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">JSONPlaceholder - Fake online REST API for developers</A>
                <DT><A HREF="https://www.google.es/search?q=lorempixel&oq=loremp&aqs=chrome.1.69i57j0l5.2737j0j7&sourceid=chrome&es_sm=122&ie=UTF-8" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">lorempixel - Buscar con Google</A>
                <DT><A HREF="https://www.google.es/search?q=mobile+friendly&oq=mobile+friendly&aqs=chrome..69i57j0l5.5309j0j7&sourceid=chrome&es_sm=122&ie=UTF-8" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">mobile friendly - Buscar con Google</A>
                <DT><A HREF="https://www.google.com/webmasters/tools/mobile-friendly/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Mobile-Friendly Test</A>
                <DT><A HREF="http://www.danstools.com/?_ga=1.199082793.742028156.1426243426" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Dans Tools - Online tools for users and developers.</A>
                <DT><A HREF="http://www.stockvault.net/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Free Stock Photos | Stockvault.net - Free Photos - Free Images</A>
                <DT><A HREF="https://codepen.io/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">CodePen - Front End Developer Playground &amp; Code Editor in the Browser</A>
                <DT><A HREF="https://developer.sony.com/develop/open-devices/get-started/unlock-bootloader/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Unlockbootloader | Step 3 / 4 - Developer World</A>
                <DT><A HREF="https://randomkeygen.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Random Key Generator</A>
                <DT><A HREF="https://www.danstools.com/?_ga=1.199082793.742028156.1426243426" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Dans Tools - Online tools for users and developers.</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971439">Tutoriales y Cursos</H3>
            <DL><p>
                <DT><A HREF="file:///C:/Users/walter/Downloads/Curso%20CI/index.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Curso codeigniter</A>
                <DT><A HREF="http://www.falconmasters.com/cursos/como-crear-un-theme-para-wordpress/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Curso de creación de un theme para wordpress (Responsive Design)</A>
                <DT><A HREF="http://www.adeje.es/uva/cursos/577-cursos-de-la-universidad-de-ve" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Cursos de la Universidad de Verano de Adeje | Cursos | Universidad de Verano | Ayuntamiento de Adeje</A>
                <DT><A HREF="https://platzi.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Platzi: Cursos online profesionales de tecnología</A>
                <DT><A HREF="http://www.quackit.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Quackit Tutorials</A>
                <DT><A HREF="http://librosweb.es/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Tutoriales de diseño y programación</A>
                <DT><A HREF="http://www.w3schools.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">W3Schools Online Web Tutorials</A>
                <DT><A HREF="https://conclase.net/mysql/curso/cap7#" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Curso de MySQL - Creación de bases de datos</A>
                <DT><A HREF="https://www.adeje.es/uva/cursos/577-cursos-de-la-universidad-de-ve" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Cursos de la Universidad de Verano de Adeje | Cursos | Universidad de Verano | Ayuntamiento de Adeje</A>
                <DT><A HREF="https://www.quackit.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Quackit Tutorials</A>
                <DT><A HREF="https://www.w3schools.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">W3Schools Online Web Tutorials</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725972321">Twitter Tools</H3>
            <DL><p>
                <DT><A HREF="http://twitterfeed.com/welcome/email_confirmation" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">twitterfeed.com : feed your blog to twitter</A>
                <DT><A HREF="http://foller.me/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Foller.me Analytics for Twitter</A>
                <DT><A HREF="https://twitterfeed.com/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">twitterfeed.com : feed your blog to twitter</A>
                <DT><A HREF="https://foller.me/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">Foller.me Analytics for Twitter</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725970842">webtest</H3>
            <DL><p>
                <DT><A HREF="http://www.webpagetest.org/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">WebPagetest - Website Performance and Optimization Test</A>
                <DT><A HREF="https://www.webpagetest.org/" ADD_DATE="1667664395" LAST_MODIFIED="1725970842">WebPagetest - Website Performance and Optimization Test</A>
            </DL><p>
            <DT><A HREF="http://www.connectionstrings.com/access#microsoft-jet-ole-db-4-0" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Access Connection String Samples - ConnectionStrings.com</A>
            <DT><A HREF="http://www.bad-neighborhood.com/text-link-tool.htm" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bad Neighborhood - Link Exchange Tool</A>
            <DT><A HREF="https://github.com/beckenrode/mysql-workbench-export-laravel-5-migrations" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">beckenrode/mysql-workbench-export-laravel-5-migrations: A MySQL Workbench plugin which exports a Model to Laravel 5 Migrations</A>
            <DT><A HREF="file:///Users/waltercervini/websites/caddy/caddyserver.com/docs.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Caddy Documentation</A>
            <DT><A HREF="http://www.clonescripts.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Clone Scripts of Popular Websites - CloneScripts.com</A>
            <DT><A HREF="http://www.cristalab.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Comunidad de diseño web y desarrollo en internet, Cristalab v4</A>
            <DT><A HREF="https://www.xml-sitemaps.com/crawl.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Create your Google Sitemap Online - XML Sitemaps Generator</A>
            <DT><A HREF="http://www.desarrolloweb.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Desarrollo Web, Tu mejor ayuda para aprender a hacer webs.</A>
            <DT><A HREF="http://en.freedownloadmanager.org/Mac-OS/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Discover the best app downloads for Mac OS X on FreeDownloadManager.org</A>
            <DT><A HREF="https://editor.datatables.net/generator/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Generator</A>
            <DT><A HREF="http://www.seomar.es/posicionamiento_web-herramientas_seo" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Herramientas de Posicionamiento Web SEO</A>
            <DT><A HREF="https://htmlpdfapi.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">HTML PDF API - Convert HTML to PDF with online REST API / HTML2PDF</A>
            <DT><A HREF="https://github.com/imsky/holder" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://github.com/imsky/holder" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACpklEQVQ4jW2SwWucVRTFf/e975uZtCElk9RIwabGaZO0FMFNK9SFexHElQu7EN0oCt0ILQquxIUiWK1Y/QcERXFbUaqrCorFWDuJTBJLGqKNHYua5Jv37nGRCR2CZ3Uf3HcP53evsS0DBDDZmnk4xvLZAI8K7gWZYauOfeWePlxauHaFAdlAXU7NHH/D4HkLoYGEJAGYmWGGXBuSznfaP50FfGdAgFY5NdP4pCjKx9wdtv8NzL/7DjGQUu/TzvW5p4AcAU1NH3irVqudTil9mZVfMWw8mO13+aqga2al0JWc8lmkPbVa/fGR0fH67fXfL9mh1uzJWBSXY1HG1Ks+6LTnXgCKI0cenKiqv9YBcr3evNFu3wKqqenjbxdl+WLOva3Uy6eKEONzFkJNnjFIQATy/PzVlQE+N/t5oqHk7tEs7AnBnwlmPIIkd21s9tJ7QO43DwLeqXOidwHPfyPJzE4FYQcMM9AfK53ri/1GHyC3Q1EAy+32b4KbZmDY/QEwIQmGm83W0C7n3bKJiYmGYEQyk1EEM5aRCGbN4bHyRN+p+J8IBaD6vrGTweweSTJYCmT/lhAA+6csio8mDx+eZRvm7gjpYOvosTLG8wAWzCR9Y5Ot2YeKovjepXeC2X0hxifc8+ee/bXF+Z+vAhxsHT1WlsXLkp4MZnuBJMlzzifC8q+//CD5+0WML1VV9brn9CZi+N+tdOeufbVpcDqY7ZXYCDEWwt9dWrj2YwBCJ2+dkfvleqP+scu/k/u5teX2zka4kdKKS2sAMcahnNIXnbR1DggDoA41HpgeuRiK8LRnZ33zzmh3aakL0Gy1RkaLoa5ZyO75Yqc9dwao6F9dn3I33V5f+2zf+P6vTbq1mqtLdLsJYOPPJqNjZT0nvbq4MHdh4Nj4D+UDSXCdrYd5AAAAAElFTkSuQmCC">imsky/holder</A>
            <DT><A HREF="https://mailtrap.io/inboxes" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Inboxes - Mailtrap</A>
            <DT><A HREF="http://ftp.redhat.com/pub/redhat/linux/enterprise/6Workstation/en/os/SRPMS/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Index of /pub/redhat/linux/enterprise/6Workstation/en/os/SRPMS</A>
            <DT><A HREF="https://yajrabox.com/docs/laravel-datatables/6.0" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Installation - Laravel Datatables YajraBox</A>
            <DT><A HREF="http://necolas.github.io/normalize.css/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Normalize.css: Make browsers render all elements more consistently.</A>
            <DT><A HREF="https://readthedocs.org/dashboard/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Panel de Proyecto | Read the Docs</A>
            <DT><A HREF="http://www.falconmasters.com/desarrollo-web/que-se-necesita-para-tener-una-pagina-web/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Que se necesita para tener una página web - FalconMasters</A>
            <DT><A HREF="https://dashboard.pusher.com/apps/267124/keys" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Pusher: clean-lawn-493 - Keys</A>
            <DT><A HREF="http://www.mysqlperformanceblog.com/2009/11/16/table_cache-negative-scalability/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">table_cache negative scalability - MySQL Performance Blog</A>
            <DT><A HREF="http://norfipc.com/redes-sociales/tamano-medida-fotos-perfil-sitios-sociales-internet.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Tamaño y medida de las fotos de perfil en los sitios sociales</A>
            <DT><A HREF="http://ayudawp.com/todo-sobre-htaccess/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Todo lo que tienes que saber sobre .htaccess y algunos trucos extra | Ayuda WordPress</A>
            <DT><A HREF="https://changelog.com/wemux-multi-user-terminal-multiplexing-for-party-pair-pr/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">wemux - multi-user terminal multiplexing for party pair programming based on tmux - The Changelog</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">wordpress</H3>
            <DL><p>
                <DT><A HREF="https://codex.wordpress.org/Plugin_Resources" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Plugin Resources « WordPress Codex</A>
                <DT><A HREF="https://developer.wordpress.org/themes/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Theme Developer Handbook | WordPress Developer Resources</A>
            </DL><p>
            <DT><A HREF="http://www.dynamicdrive.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Dynamic Drive DHTML(dynamic html) &amp; JavaScript code library</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Graficos</H3>
            <DL><p>
                <DT><A HREF="http://ww25.templated.co/?subid1=20211122-0255-4730-bf7e-dcd45d536bf0" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">TEMPLATED - Free CSS, HTML5 and Responsive Site Templates</A>
            </DL><p>
            <DT><A HREF="https://specificity.keegan.st/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Specificity Calculator</A>
            <DT><A HREF="https://bundlers.tooling.report/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Overview | Tooling.Report</A>
            <DT><A HREF="https://modern-web.dev/docs/test-runner/browser-launchers/overview/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Browser Launchers: Overview: Modern Web</A>
            <DT><A HREF="https://2x.antdv.com/docs/vue/customize-theme" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Ant Design Vue</A>
            <DT><A HREF="https://quasar.dev/vue-components/bar" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bar | Quasar Framework</A>
            <DT><A HREF="https://lenguajejs.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Lenguaje Javascript | Documentación sobre programación web - Javascript en español - Lenguaje JS</A>
            <DT><A HREF="https://terminaldelinux.com/terminal/introduccion/instalacion-zsh/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Instalación de zsh - Línea de comandos en español - Terminal de Linux</A>
            <DT><A HREF="https://github.com/powerline/fonts" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">powerline/fonts: Patched fonts for Powerline users.</A>
            <DT><A HREF="https://www.youtube.com/watch?v=G5DD_qLxbo8" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">(7) Tmux | Multiplexor de Terminales para programadores, Sys Admins y Hackers - YouTube</A>
            <DT><A HREF="https://www.twitch.tv/crackotv" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CrackoTV - Twitch</A>
            <DT><A HREF="https://www.youtube.com/watch?v=8XGueeQJsrA" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">(27) Plugin Showcase: Ctrl-P - YouTube</A>
            <DT><A HREF="https://www.tradingview.com/pine-script-reference/v5/#fun_line{dot}new" ADD_DATE="1667873599" LAST_MODIFIED="1724671971">Pine Script Language Reference Manual — TradingView</A>
            <DT><A HREF="https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify" ADD_DATE="1656250499" LAST_MODIFIED="1724671971">JSON.stringify() - JavaScript | MDN</A>
            <DT><A HREF="https://awesomejs.dev/" ADD_DATE="1656250512" LAST_MODIFIED="1724671971">Awesome JS</A>
            <DT><A HREF="https://practicalpython.yasoob.me/toc.html" ADD_DATE="1666421477" LAST_MODIFIED="1724671971">Tabla de contenido - Proyectos prácticos de Python</A>
            <DT><A HREF="https://automatetheboringstuff.com/#toc" ADD_DATE="1666421526" LAST_MODIFIED="1724671971">Automate the Boring Stuff with Python</A>
            <DT><A HREF="https://christitus.com/vm-setup-in-linux/" ADD_DATE="1667212902" LAST_MODIFIED="1724671971">Setup Qemu in Debian Linux</A>
            <DT><A HREF="https://leetcode.com/" ADD_DATE="1666558500" LAST_MODIFIED="1724671971">LeetCode - The World&#39;s Leading Online Programming Learning Platform</A>
            <DT><A HREF="https://matplotlib.org/stable/index.html" ADD_DATE="1666430219" LAST_MODIFIED="1724671971">Matplotlib documentation — Matplotlib 3.6.0 documentation</A>
            <DT><A HREF="https://twopirllc.github.io/pandas-ta/" ADD_DATE="1666431202" LAST_MODIFIED="1724671971">pandas-ta | Technical Analysis Indicators - Pandas TA is an easy to use Python 3 Pandas Extension with 130+ Indicators</A>
            <DT><A HREF="https://numpy.org/doc/stable/index.html" ADD_DATE="1666431211" LAST_MODIFIED="1724671971">Documentación de NumPy — Manual de NumPy v1.23</A>
            <DT><A HREF="https://book.pythontips.com/_/downloads/en/latest/pdf/#page=51&zoom=auto,-26,836" ADD_DATE="1666431224" LAST_MODIFIED="1724671971">Python Tips - book-pythontips-com-en-latest.pdf</A>
            <DT><A HREF="https://docs.python.org/es/3/" ADD_DATE="1666432666" LAST_MODIFIED="1724671971">3.10.8 Documentation</A>
            <DT><A HREF="file:///home/v0lp/libros/HTML/pandas/index.html" ADD_DATE="1666432576" LAST_MODIFIED="1724671971">pandas documentation — pandas 1.5.1 documentation</A>
            <DT><A HREF="https://scikit-learn.org/stable/" ADD_DATE="1666432852" LAST_MODIFIED="1724671971">scikit-learn: machine learning in Python — scikit-learn 1.1.2 documentation</A>
            <DT><A HREF="https://leetcode.com/problems/sudoku-solver/" ADD_DATE="1666562010" LAST_MODIFIED="1724671971">(1) Sudoku Solver - LeetCode</A>
            <DT><A HREF="https://docs.python.org/3.9/" ADD_DATE="1668026957" LAST_MODIFIED="1724671971" TAGS="python">3.9.14 Documentation</A>
            <DT><A HREF="file:///home/v0lp/Descargas/sqlalchemy_14/index.html" ADD_DATE="1668951313" LAST_MODIFIED="1724671971">SQLAlchemy Documentation — SQLAlchemy 1.4 Documentation</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bash</H3>
            <DL><p>
                <DT><A HREF="https://ss64.com/bash/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">bash commands - Linux MAN Pages</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971498">Frameworks</H3>
            <DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Cake-php</H3>
                <DL><p>
                    <DT><A HREF="https://techtastico.com/post/lo-nuevo-en-cakephp-12-y-las-diferencias-con-cakephp-11/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Lo nuevo en CakePHP 1.2 y las diferencias con CakePHP 1.1</A>
                    <DT><A HREF="https://techtastico.com/post/tutoriales-muy-utiles-de-cakephp/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Tutoriales muy útiles de CakePHP</A>
                    <DT><A HREF="https://techtastico.com/post/manual-descarga-cakephp-1.2/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Manual de CakePHP 1.2 y descarga versión final</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971498">CodeIgniter</H3>
                <DL><p>
                    <DT><A HREF="https://code.tutsplus.com/categories/codeigniter" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CodeIgniter - Tuts+ Code Category</A>
                    <DT><A HREF="https://www.daharveyjr.com/tag/codeigniter/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">CodeIgniter Archives - @daharveyjr</A>
                    <DT><A HREF="https://datamapper.wanwizard.eu/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">DataMapper ORM - User Guide</A>
                    <DT><A HREF="https://forums.grocerycrud.com/topic/2682-dependent-drop-down-with-multiselect/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Dependent Drop Down With Multiselect - I have a question - grocery CRUD forum</A>
                    <DT><A HREF="https://expressionengine.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ExpressionEngine - Publish Your Universe!</A>
                    <DT><A HREF="https://app.assembla.com/wiki/show/IgnitedRecord" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Home | IgnitedRecord | Assembla</A>
                    <DT><A HREF="https://sumonbd.wordpress.com/2009/10/04/jq-grid-with-codeigniter/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">JQ Grid with Codeigniter « PathFinder&#39;s Weblog</A>
                    <DT><A HREF="https://forums.grocerycrud.com/topic/1561-simple-dependant-dropdown-extension/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Simple dependant dropdown extension - Extra coding / Plugins - grocery CRUD forum</A>
                    <DT><A HREF="https://afruj.wordpress.com/2008/05/02/some-codeigniter-tutorial-links/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Some CodeIgniter Tutorial links « The Brook Song – ঝর্ণার গান</A>
                    <DT><A HREF="https://www.web-design-talk.co.uk/493/codeigniter-base-models-rock/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Why Codeigniter Base Models (MY_Model) Rock</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971498">laravel</H3>
                <DL><p>
                    <DT><A HREF="https://infyom.com/open-source/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">InfyOm Laravel Generator : Laravel Scaffold, CRUD, API Generator</A>
                    <DT><A HREF="http://ww1.laravel-recipes.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Laravel Recipes :: Rendering a View For Items in a Collection</A>
                    <DT><A HREF="https://mattstauffer.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Matt Stauffer on Laravel, PHP, Frontend development</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">phppixie</H3>
                <DL><p>
                    <DT><A HREF="https://phpixie.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">PHPixie Framework | Fast PHP Framework</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Symfony</H3>
                <DL><p>
                    <DT><A HREF="https://symfoniac.wordpress.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Symfoniac</A>
                    <DT><A HREF="https://symfony.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://symfony.com/" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACMElEQVQ4jW2TvUscURTFf+/tjuPigCPI2gh2sVNEjANaaLGgi3ZWNnapUwSxs7MRTRZBMF06/4AUWoidhQgiCAmIBE2xYLHdrrKz806KvFlWkwMXLo9zP96598K/mAOOgJ9A09sP/zb7H34XfcAX4BlQr1lrc/8Z2PPcLiwQAqee5IAUyLzvgKxYLKbDw8POc059Emt8ks/AR6BtrS065yygQqFAlmVMTk5SqVRMqVRy8/PzneXl5T7n3B7wCeA98AJ0fFUNDAy4OI7lfV1fXytJEheGoba3tzNjTMfHTAN8BWSMSQG3trbmDg8PtbGxoSRJtLW1pbu7OwFaX1/Pv5T6rxzh1XZAFoah2u22Njc3BWhhYUGtVkvHx8caHx/XycmJoihSjz63+DHl4rmbmxs1Gg2NjY2pXC5Lkg4ODjQzM6P+/v4uz8c0sdY2AVWrVVer1dzo6KiazaZ2d3e1srKiLMtUrVZ7x/oqgZX0G9DT05NGRkZMFEU8Pj5ydnbG1NQU1lqurq4wxmCMATA9yX51RQTSOI7d0tKSm5iYEKCLiwtdXl7Ki9xb/ZWI08CLH02Wtzk4OKg0TbW6uppvY9525kf+AkwXgDoQA3NBEKT1et00Gg27uLio+/t79vf3McYgyfjqHSAAasC3gl/lc2DWWvtuaGiIKIqyh4cHs7Ozk29qXtkCReA78IE3CPh7KM9BELw6ph7Ljyl4G9xFqVRKgCNr7S3Q8nbrBUve8v8AjIUTNEng598AAAAASUVORK5CYII=">symfony-forge.com - site dedicated to symfony plugins</A>
                    <DT><A HREF="https://symfony.es/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Symfony.es</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971498">yii</H3>
                <DL><p>
                </DL><p>
                <DT><A HREF="https://code.tutsplus.com/tutorials/6-codeigniter-hacks-for-the-masters--net-8308" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">6 CodeIgniter Hacks for the Masters - Tuts+ Code Tutorial</A>
                <DT><A HREF="https://frameworkphp.wordpress.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Framework PHP</A>
                <DT><A HREF="http://18382.whserv.de/admin/index.php" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Yellow Duck Framework</A>
            </DL><p>
            <DT><A HREF="https://manuals.setasign.com/fpdi-manual/v1/the-fpdi-class/examples/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Examples</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971498">PHP</H3>
            <DL><p>
                <DT><A HREF="https://onlinephp.io/preg-match" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">preg_match Info, execute, run and test online</A>
                <DT><A HREF="https://www.0php.com/free_PHP_webhosting.php" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">free PHP webhosting servers</A>
                <DT><A HREF="https://picandocodigo.wordpress.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">picandoCodigo();</A>
                <DT><A HREF="http://case-5-19-cv-07071-svk.info/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">xajax PHP Class Library - The easiest way to develop asynchronous Ajax applications with PHP</A>
                <DT><A HREF="http://php.resourceindex.com/tips_and_tutorials/examples_and_tutorials/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">The PHP Resource Index: Documentation: Examples and Tutorials</A>
                <DT><A HREF="https://www.hotscripts.com/PHP/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Hotscripts.com :: PHP</A>
                <DT><A HREF="https://astec.net/?geo=es" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">phpguru.org - Home</A>
                <DT><A HREF="https://phpbuilder.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">PHPBuilder.com, the best resource for PHP tutorials, templates, PHP manuals, content management systems, scripts, classes and more.</A>
                <DT><A HREF="https://www.tinybutstrong.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">TinyButStrong</A>
                <DT><A HREF="https://www.yiiframework.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Yii PHP Framework: Best for Web 2.0 Development</A>
                <DT><A HREF="https://www.phpmydirectory.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">phpMyDirectory.com - PHP/mySQL Business Directory Script - PHP/mySQL Yellow Pages Script - PHP Directory Project</A>
                <DT><A HREF="https://astec.net/?geo=hk" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">phpguru.org - Home</A>
            </DL><p>
            <DT><A HREF="https://www.connectionstrings.com/access/#microsoft-jet-ole-db-4-0" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Access Connection String Samples - ConnectionStrings.com</A>
            <DT><A HREF="https://blog.atom.io/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Atom Blog</A>
            <DT><A HREF="https://www.vultr.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Clone Scripts of Popular Websites - CloneScripts.com</A>
            <DT><A HREF="https://desarrolloweb.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Desarrollo Web, Tu mejor ayuda para aprender a hacer webs.</A>
            <DT><A HREF="https://en.freedownloadmanager.org/Mac-OS/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Discover the best app downloads for Mac OS X on FreeDownloadManager.org</A>
            <DT><A HREF="https://www.seomar.es/posicionamiento_web-herramientas_seo/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Herramientas de Posicionamiento Web SEO</A>
            <DT><A HREF="https://ftp.redhat.com/pub/redhat/linux/enterprise/6Workstation/en/os/SRPMS/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Index of /pub/redhat/linux/enterprise/6Workstation/en/os/SRPMS</A>
            <DT><A HREF="https://www.c-sharpcorner.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Learn C#, WPF, Visual Studio 2012, Windows 8, TypeScript, HTML 5, Windows Phone 8, ASP.NET, WCF</A>
            <DT><A HREF="https://readthedocs.org/accounts/login/?next=/dashboard/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Panel de Proyecto | Read the Docs</A>
            <DT><A HREF="https://dashboard.pusher.com/accounts/sign_in" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Pusher: clean-lawn-493 - Keys</A>
            <DT><A HREF="https://www.percona.com/blog/2009/11/16/table_cache-negative-scalability/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">table_cache negative scalability - MySQL Performance Blog</A>
            <DT><A HREF="https://norfipc.com/redes-sociales/tamano-medida-fotos-perfil-sitios-sociales-internet.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Tamaño y medida de las fotos de perfil en los sitios sociales</A>
            <DT><A HREF="https://ayudawp.com/todo-sobre-htaccess/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Todo lo que tienes que saber sobre .htaccess y algunos trucos extra | Ayuda WordPress</A>
            <DT><A HREF="http://ww1.ebooks-space.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Visual Basic eBooks » FREE eBooks Download » Visual Basic Ebooks Free download site page 3</A>
            <DT><A HREF="https://changelog.com/posts/wemux-multi-user-terminal-multiplexing-for-party-pair-pr" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">wemux - multi-user terminal multiplexing for party pair programming based on tmux - The Changelog</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Editores</H3>
            <DL><p>
                <DT><A HREF="https://granneman.com/webdev/editors/sublime-text/configuring-sublime-text" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Configuring Sublime Text :: Scott Granneman</A>
            </DL><p>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ruby</H3>
            <DL><p>
                <DT><A HREF="https://rubular.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Rubular: a Ruby regular expression editor and tester</A>
                <DT><A HREF="https://rlbisbe.net/2012/02/27/sinatra-un-framework-web-para-ruby/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Sinatra, un framework web para Ruby | rlbisbe @ dev</A>
                <DT><A HREF="https://apidock.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Front page - APIdock</A>
                <DT><A HREF="https://rubyonrails.org.es/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Ruby on Rails - El desarrollo web que no molesta</A>
                <DT><A HREF="https://github.com/rbenv/rbenv#how-it-works" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">sstephenson/rbenv · GitHub</A>
                <DT><A HREF="https://github.com/rbenv/ruby-build#readme" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">sstephenson/ruby-build · GitHub</A>
                <DT><A HREF="https://guides.rubyonrails.org/active_record_validations.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Active Record Validations — Ruby on Rails Guides</A>
                <DT><A HREF="https://rubyonrails.org/2012/3/21/strong-parameters" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Riding Rails: Strong parameters: Dealing with mass assignment in the controller instead of the model</A>
                <DT><A HREF="https://guides.rubyonrails.org/routing.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Rails Routing from the Outside In — Ruby on Rails Guides</A>
            </DL><p>
            <DT><A HREF="https://www.afternic.com/forsale/CLONESCRIPTS.COM?utm_source=TDFS&utm_medium=sn_affiliate_click&utm_campaign=TDFS_GoDaddy_DLS&traffic_type=TDFS&traffic_id=GoDaddy_DLS" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Clone Scripts of Popular Websites - CloneScripts.com</A>
            <DT><A HREF="https://www.freqtrade.io/en/stable/rest-api/" ADD_DATE="1665788577" LAST_MODIFIED="1724671971">REST API &amp; FreqUI - Freqtrade</A>
            <DT><A HREF="https://www.freqtrade.io/en/stable/exchanges/" ADD_DATE="1666117800" LAST_MODIFIED="1724671971">Exchange-specific Notes - Freqtrade</A>
        </DL><p>
        <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971708">Aeromodelismo</H3>
        <DL><p>
            <DT><A HREF="https://aisler.net/fritzing" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">AISLER - Powerful Prototyping for your electronics project made in Germany.</A>
            <DT><A HREF="http://radiocontrol.es/contentid-72.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Alas volantes - Aeromodelismo RadioControl, Radiocontrol.es</A>
            <DT><A HREF="https://jlcpcb.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">PCB Prototype &amp; PCB Fabrication Manufacturer - JLCPCB</A>
            <DT><A HREF="https://outerzone.co.uk/index.asp" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Oz : Free plans : Collection of free vintage model aircraft plans to download</A>
            <DT><A HREF="https://www.liveabout.com/free-glider-plans-4158613" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Free Downloadable Glider Airplane Plans</A>
            <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971708">Acrilico</H3>
            <DL><p>
                <DT><A HREF="http://www.tucortecnc.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Bienvenidos a tucorteCNC.com!!!!</A>
                <DT><A HREF="http://www.melevsreef.com/acrylics/overflow.html" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">DIY Overflow Box</A>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1725971708">teclados qmk</H3>
                <DL><p>
                    <DT><A HREF="https://docs.qmk.fm/#/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">QMK Firmware</A>
                    <DT><A HREF="https://www.littlekeyboards.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Pequeños teclados</A>
                    <DT><A HREF="https://config.qmk.fm/#/0xcb/tutelpad/LAYOUT" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">QMK Configurator</A>
                    <DT><A HREF="https://github.com/qmk/qmk_toolbox" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">qmk/qmk_toolbox: A Toolbox companion for QMK Firmware</A>
                    <DT><A HREF="https://qmk.fm/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">QMK Firmware - An open source firmware for AVR and ARM based keyboards</A>
                    <DT><A HREF="https://splitkb.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">splitkb.com - All about split keyboards.</A>
                    <DT><A HREF="https://github.com/pierrechevalier83/ferris" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">pierrechevalier83/ferris: A low profile split keyboard designed to satisfy one single use case elegantly</A>
                    <DT><A HREF="https://shop.keyboard.io/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Keyboardio: keyboards for serious typists</A>
                    <DT><A HREF="https://www.littlekeyboards.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Little Keyboards</A>
                    <DT><A HREF="https://www.keyboard.university/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Keyboard University</A>
                    <DT><A HREF="https://keyhive.xyz/shop" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Shop — KeyHive</A>
                    <DT><A HREF="https://github.com/rogerclarkmelbourne/STM32duino-bootloader" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">STM32duino-bootloader/binaries at master · rogerclarkmelbourne/STM32duino-bootloader</A>
                    <DT><A HREF="https://github.com/ruiqimao/keyboard-pcb-guide" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">ruiqimao/keyboard-pcb-guide: Guide on how to design keyboard PCBs with KiCad</A>
                </DL><p>
                <DT><H3 ADD_DATE="1667664395" LAST_MODIFIED="1724671971">audiovisuales</H3>
                <DL><p>
                    <DT><A HREF="https://ncs.io/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">NCS (NoCopyrightSounds) - free music for content creators</A>
                    <DT><A HREF="https://www.ncs-spain.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">NCS Spain | Consultoría Tecnológica comprometida con la Innovación</A>
                    <DT><A HREF="https://polygonrunway.com/p/become-a-3d-illustrator-in-one-hour" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Learn 3D illustration with the free Blender beginner course | Polygon</A>
                </DL><p>
                <DT><A HREF="http://www.blogmecanicos.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Blog Mecánicos</A>
                <DT><A HREF="https://www.drogueriaelbarco.com/content/terminos-y-condiciones-de-uso" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Términos y condiciones</A>
                <DT><A HREF="https://riptutorial.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Learn programming languages with books and examples</A>
                <DT><A HREF="https://www.cosmeticstenerife.es/search?type=product&q=Aceite+Esencial+de+Cajeput+&options%5Bprefix%5D=last" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Resultados de la búsqueda: 0 resultados para &quot;Aceite Esencial de Cajeput &quot;</A>
                <DT><A HREF="https://play.typeracer.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">TypeRacer - Play Typing Games and Race Friends</A>
                <DT><A HREF="https://3d.homestyler.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Homestyler - Floor plan creator &amp; Free online home design software</A>
                <DT><A HREF="https://monkeytype.com/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Monkeytype</A>
                <DT><A HREF="https://orangetv.orange.es/lcn?extChId=1011&type=live" ADD_DATE="1667664395" LAST_MODIFIED="1724671971" ICON_URI="fake-favicon-uri:https://orangetv.orange.es/brw" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAAc0lEQVQ4jWP8X8lAEmAiTfmohsGigQVK/ydCLSNcAyMTg0kig4Q+w/+/OJQyM7y4yHB2PsP/fzANmr4Mmv74jL++keHcQpiG//8ZHp9iYGTGZ8PjUwz//zMwMDBCUysjMwMjIz4b/v+HGAf39F+i/M3AAAB83CJUD5vU4QAAAABJRU5ErkJggg==">Ver Orange TV online en tu ordenador, tablet o móvil</A>
                <DT><A HREF="https://www.typing.com/es/student/lessons" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Lecciones de Tecleo - Aprende a Escribir y Mejora la Velocidad de Escritura Gratis - Typing.com</A>
                <DT><A HREF="https://zmk.dev/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">Hello from ZMK Firmware | ZMK Firmware</A>
                <DT><A HREF="https://www.engbedded.com/fusecalc/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">AVR® Fuse Calculator – The Engbedded Blog</A>
                <DT><A HREF="https://www3.gobiernodecanarias.org/dragoweb/" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">miHistoria - Inicio</A>
            </DL><p>
            <DT><A HREF="https://www.hta3d.com/es/kit-de-perfiles-de-aluminio-para-hypercube-evolution-eje-z-dual-hevo-para-volumen-de-impresion-30-x-30-x-30-cm-aprox" ADD_DATE="1667664395" LAST_MODIFIED="1724671971">▷Kit de Perfiles de Aluminio para HyperCube Evolution eje Z dual - HEVO - Para volumen de impresión 30 x 30 x 30 cm aprox - HTA3D ✅</A>
        </DL><p>
    </DL><p>
</DL>
'''

def get_attr(data_container, attr:str):
	for bookmark in data_container:
		for dat in bookmark.find_all(attr.lower()):
			if dat.text:
				new_data=dat.text.lower()
				if new_data not in unique_data:
					unique_data.append(new_data)

def find_unique_data(key:str,value:str):
	for data in unique_data:
		if data.get(key)==value:
			return True
	return False



def load_bookmark(filename: str) -> BeautifulSoup:
	with open(filename, encoding="utf8") as file:
		return BeautifulSoup(file,features= "html.parser")


unique_data = []
html_content = load_bookmark("bookmarks.html")

