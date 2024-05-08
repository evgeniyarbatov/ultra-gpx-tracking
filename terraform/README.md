Init 

```
tf init
```

Deploy:

```
tf apply -auto-approve
```

## CloudFront config

Import existing CloudFront config:

```
import {
  to = aws_cloudfront_distribution.cloudfront
  id = "E2ABRC7WI48APW"
}
```

with:

```
terraform plan -generate-config-out=import.tf
```

and add it to the state:

```
tf import aws_cloudfront_distribution.cloudfront E2ABRC7WI48APW
```

In import.tf define:

```
  lifecycle {
    prevent_destroy = true
  }
  ordered_cache_behavior {
    path_pattern           = "/sg200/*"
    allowed_methods        = ["GET", "HEAD", "OPTIONS"]
    cached_methods         = ["GET", "HEAD", "OPTIONS"]
    target_origin_id       = "${aws_instance.server.id}-origin"
    viewer_protocol_policy = "redirect-to-https"

    min_ttl     = 0
    default_ttl = 0
    max_ttl     = 0
    compress    = true

    forwarded_values {
      query_string = false
      headers      = ["Origin"]

      cookies {
        forward = "all"
      }
    }
  }
  origin {
    domain_name              = aws_instance.server.public_dns
    origin_id                = "${aws_instance.server.id}-origin"
    custom_origin_config {
      http_port = 80
      https_port = 443
      origin_protocol_policy = "match-viewer"
      origin_ssl_protocols = ["TLSv1"]
    }
  }
```