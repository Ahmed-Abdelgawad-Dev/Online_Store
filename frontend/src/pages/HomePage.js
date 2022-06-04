import React from "react";
import { Col, Container, Row } from "react-bootstrap";
import Product from "../components/Product.js";
import { products } from "../dummy.js";
import { Link } from "react-router-dom";
export default function HomePage() {
  return (
    <>
      <h1>Products' List</h1>
      <Link to="/test">Test</Link>
      <div>
        <Container>
          <Row>
            {products.map((product) => (
              <Col key={product._id}>
                <div class="d-flex justify-content-start">
                  <Product product={product} />
                </div>
              </Col>
            ))}
          </Row>
        </Container>
      </div>
    </>
  );
}
