import React from "react";
import { Col, Row } from "react-bootstrap";
import { Link, useParams } from "react-router-dom";
import { products } from "../dummy";
import Rating from "./Rating";

export default function ProductDetails() {
  const { id } = useParams();
  const product = products.find((prod) => Number(prod._id) === Number(id));
  return (
    <div className="fluid">
      <Link to="/" className="btn btn-primary my-3">
        Back
      </Link>
      <div className="container">
        <div className="row">
          <div className="col-md-6">
            <img
              className="img-fluid sm-3 p-2 rounded img-responsive"
              src={product?.image}
              alt={product?.image || "product image"}
            ></img>
          </div>
          <div className="col-md-3">
            <ul className="list-group list-group-flush">
              <li className="list-group-item">
                <h3 className=" overflow-hidden">{product?.name}</h3>
              </li>
              <li className="list-group-item">
                <Rating
                  value={product.rating}
                  text={`${
                    product.reviewsCount ? product.reviewsCount : "No"
                  } reviews`}
                />
              </li>
              <li className="list-group-item">
                <strong>${product.price}</strong>
              </li>
              <li className="list-group-item">{product.description}</li>
            </ul>
          </div>
          <div className="col-md-3">
            <ul className="list-group">
              <li className="list-group-item">
                <div className="row">
                  <div className="col">Price</div>
                  <div className="col">${product.price}</div>
                </div>
              </li>
              <li className="list-group-item">
                <div className="row">
                  <div className="col">Available:</div>
                  <div className="col">
                    {product.stockCount > 0 ? "Yes" : "No"}
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
