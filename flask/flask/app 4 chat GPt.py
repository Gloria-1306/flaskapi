from flask import jsonify, abort

@app.route("/product_name/<int:product_id>")
def products(product_id):
    try:
        db_conn = pymysql.connect(host="localhost", user="root", password='Glojai29ans!', database="make_up", cursorclass=pymysql.cursors.DictCursor)

        with db_conn.cursor() as cursor:
            cursor.execute(""" 
                SELECT
                    e.product_id,
                    e.product_name, 
                    e.brand,
                    e.price,
                    e.size,
                    e.rating,
                    e.noofratings 
                FROM e_cosmetic as e
                INNER JOIN product_tab as p
                ON e.product_name = p.product_name
                WHERE e.product_id = %s
                ORDER BY e.rating DESC
                """, (product_id,))
            product = cursor.fetchone()

        db_conn.close()

        if product is None:
            abort(404)  # Product not found

        return jsonify(product)
    except Exception as e:
        abort(500)  # Internal server error
