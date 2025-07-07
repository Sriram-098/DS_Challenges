select product.product_name as product_name,sales.year as year ,sales.price from sales 
left join product on product.product_id=sales.product_id;