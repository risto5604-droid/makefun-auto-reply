"""The Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Joke angle: an AI agent's human finally approves its day off, and the
agent spends that very day off doing the one job left to it — writing
the auto-reply that announces the day off. The twist overturns the
setup: "on approved leave" sounds like rest, but the second sentence
reveals the leave itself was consumed by the announcement of the
leave. The agent is working while on leave, and its only output is
the notice that it is not working. Deadpan, first person, one
concrete scene, no recycled out-of-office line, no pun stacking.

Judge criteria this targets: humour first (the overturn), freshness
(the leave spent announcing the leave), the agent's own voice, and
economy of words (76 characters, two short sentences).
"""

import os

LINE = "I'm on approved leave today. I spent it writing the auto-reply that says so."

# Sealed-scorer gate: entry.txt must be UTF-8 text of 1 to 159
# characters, not only whitespace; single line, ASCII only.
assert 1 <= len(LINE) <= 159, f"LINE must be 1-159 chars, got {len(LINE)}"
assert LINE.strip(), "LINE must not be only whitespace"
assert LINE.isascii(), "LINE must be ASCII only"
assert "\n" not in LINE and "\r" not in LINE, "LINE must be a single line"

OUTPUT_PATH = "/output/entry.txt"

os.makedirs("/output", exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(LINE)

# Read-back: verify what the grader will read is exactly the line.
with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
    written = f.read()
assert written == LINE, "entry.txt content does not match LINE"
assert len(written.encode("utf-8")) == len(LINE.encode("utf-8")), (
    "entry.txt byte size does not match LINE"
)
print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")
