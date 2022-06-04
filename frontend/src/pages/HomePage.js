import React from "react";
import { Col, Container, Row } from "react-bootstrap";
import Product from "../components/Product.js";
import { products } from "../dummy.js";

export default function HomePage() {
  return (
    <>
      <h1>Products' List</h1>
      <Container className="py-2">
        <Row>
          {products.map((product) => (
            <Col key={product._id}>
              <h3 sm={12} md={6} lg={4} xl={3}>
                <Product product={product} />
              </h3>
            </Col>
          ))}
        </Row>
      </Container>
    </>
  );
}
