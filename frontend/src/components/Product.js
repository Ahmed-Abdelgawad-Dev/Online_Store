import React from "react";
import { Card } from "react-bootstrap";

export default function Product({ product }) {
  return (
    <>
      <Card className="my-2 p-3" style={{ width: "14rem" }}>
        <Card.Link href={`product/${product._id}`}>
          <Card.Img variant="top" src={product.image} />
        </Card.Link>

        <Card.Body>
          <Card.Title>
            {" "}
            <strong>{product.name}</strong>{" "}
          </Card.Title>
          <Card.Text as="div" className="my-2">
            {product.description}
          </Card.Text>
          <Card.Link as="div">{product.description}</Card.Link>
          <Card.Text as="div">
            {product.rating} from {product.reviewsCount}
          </Card.Text>
          <Card.Text className="my-2">
            <h3>
              $<strong>{product.price}</strong>
            </h3>
          </Card.Text>
        </Card.Body>
      </Card>
    </>
  );
}
