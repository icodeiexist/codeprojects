import mnemo,psycopg2

conn = psycopg2.connect("dbname=postgres port=5433 user=postgres")
cur = conn.cursor()
m = mnemo.major()
while True:
	cur.execute("SELECT word FROM word ORDER BY random() limit 1")
	word = cur.fetchone()
	code = m.encode(word[0])
	attempt = ""
	while attempt != code:
		print word[0]
		attempt = raw_input()
		if attempt == "exit":
			break
	if attempt == "exit":
		break
cur.close()
conn.close()
