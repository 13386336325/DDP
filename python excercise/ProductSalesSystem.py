class ProductSalesSystem:
    def __init__(self):
        # Initialize product database
        self.products = {}

    # Product Database Functions
    def add_product(self, product_id, name, price):
        """Add a new product to the database."""
        if product_id not in self.products:
            self.products[product_id] = {
                "name": name, 
                "price": price, 
                "sales_history": [],
                "feedback": []
            }
        else:
            print("Product ID already exists.")

    # Sales Tracking Functions
    def record_sale(self, product_id, quantity):
        """Record a sales transaction."""
        if product_id in self.products:
            self.products[product_id]["sales_history"].append(quantity)
        else:
            print("Product ID does not exist.")

    def calculate_total_sales(self, product_id):
        """Calculate total sales for a product."""
        if product_id in self.products:
            return sum(self.products[product_id]["sales_history"])
        else:
            print("Product ID does not exist.")
            return 0

    def identify_best_selling_product(self):
        """Identify the best-selling product."""
        best_selling_product = None
        max_sales = 0
        for product_id, product_info in self.products.items():
            total_sales = sum(product_info["sales_history"])
            if total_sales > max_sales:
                max_sales = total_sales
                best_selling_product = product_id
        return best_selling_product

    # Customer Management Functions
    def record_customer_feedback(self, product_id, rating):
        """Record customer feedback."""
        if product_id in self.products:
            self.products[product_id]["feedback"].append(rating)
        else:
            print("Product ID does not exist.")

    def calculate_average_rating(self, product_id):
        """Calculate the average rating for a product."""
        if product_id in self.products and self.products[product_id]["feedback"]:
            return sum(self.products[product_id]["feedback"]) / len(self.products[product_id]["feedback"])
        else:
            print("Product ID does not exist or no feedback available.")
            return 0

    # Reporting System
    def generate_sales_report(self):
        """Generate a report of product sales."""
        report = "Sales Report:\n"
        total_revenue = 0
        for product_id, product_info in self.products.items():
            product_revenue = sum(product_info["sales_history"]) * product_info["price"]
            total_revenue += product_revenue
            report += f"- {product_info['name']} (ID: {product_id}): Revenue = {product_revenue}\n"
        report += f"Total Revenue: {total_revenue}"
        return report

# Example usage
system = ProductSalesSystem()
system.add_product("P001", "Product 1", 10)
system.add_product("P002", "Product 2", 15)

system.record_sale("P001", 3)
system.record_sale("P001", 2)
system.record_sale("P002", 5)

system.record_customer_feedback("P001", 4)
system.record_customer_feedback("P001", 5)
system.record_customer_feedback("P002", 3)

print(system.generate_sales_report())