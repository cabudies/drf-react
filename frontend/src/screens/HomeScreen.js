import React, { useState, useEffect }  from 'react'
import { Row, Col } from 'react-bootstrap'
import Product from "../components/Product";
import axios from 'axios';

import products from '../products'


function HomeScreen() {
  const [products, setProducts] = useState([]);

  useEffect(()=> {
    async function fetchProductsFromAPI() {
      const { data } = await axios.get("/api/products")
      setProducts(data)
    }

    fetchProductsFromAPI()
  }, [])

  return (
    <div>
        <h1>Latest Products</h1>
        <Row>
            {products.map(product => (
                <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
                    {/* <h3>{product.name}</h3> */}
                    <Product product={product}/>
                </Col>
            ))}
        </Row>
    </div>
  )
}

export default HomeScreen