# Fast-Fatoora API Guide

## Endpoints

### POST /api/v1/generate-qr
Generates a Base64-encoded ZATCA TLV string and QR code image.

#### Parameters
- seller_name (string): Name of seller
- vat_number (string): 15 digit VAT number
- timestamp (ISO-8601): Invoice time
- invoice_total (string): Total amount
- vat_total (string): VAT amount