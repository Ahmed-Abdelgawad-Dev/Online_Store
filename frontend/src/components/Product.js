import React from "react";
import { Card } from "react-bootstrap";
import Rating from "./Rating";
import { Link } from "react-router-dom";

export default function Product({ product }) {
  return (
    <>
      <div className="card my-2 px-3 pb-0 pt-2" style={{ width: "14rem" }}>
        <Link to={`product/${product._id}`}>
          <img
            className="card-image-top"
            src={product?.image}
            alt={product.name}
          />
        </Link>

        <Card.Body>
          <Link to={`product/${product._id}`}>
            <Card.Title>
              {" "}
              <strong>{product.name}</strong>{" "}
            </Card.Title>
          </Link>
          <Card.Text as="div" className="my-2">
            {product.description}
          </Card.Text>
          <Card.Text as="div">
            <Rating
              value={product.rating}
              text={`${
                product.reviewsCount ? product.reviewsCount : "No"
              } reviews`}
            />
          </Card.Text>
          <Card.Text as="div" className="my-2">
            <h3>
              $<strong>{product.price}</strong>
            </h3>
          </Card.Text>
        </Card.Body>
      </div>
    </>
  );
}
