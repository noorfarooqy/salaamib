<template>
  <div class="no-stickybar">
    <div class="main-wrapper invoice-one">
      <div class="container">
        <div class="invoice-wrapper download_section">
          <div class="inv-content">
            <span class="line"></span>
            <div class="invoice-header">
              <div class="inv-header-left">
                <h4>Invoice</h4>
                <div class="company-details">
                  <div class="gst-details">
                    <h6>Dreams Technologies Pvt Ltd</h6>
                    <span
                      >Address:15 Hodges Mews,<br />
                      High Wycombe HP12 3JL, United Kingdom.</span
                    >
                  </div>
                  <div class="address-bg"></div>
                </div>
              </div>
              <div class="inv-header-right">
                <a href="javascript:;">
                  <img src="@/assets/img/logo2.png" alt="Logo" />
                </a>
                <h6>Invoice No : <span> #005</span></h6>
                <h6>Invoice Date :<span> 07-10-2023</span></h6>
                <p><span>Due Date : 07-12-2023</span></p>
              </div>
            </div>
            <span class="line"></span>
            <h5>Customer Information</h5>
            <div class="patient-infos">
              <div class="row">
                <div class="col-sm-4">
                  <div class="patient-detailed">
                    <div class="bill-add">Customer Details :</div>
                    <div class="customer-name">
                      John Williams
                      <p><span>GSTIN : ACWR000054321</span></p>
                    </div>
                    <div class="payment-status">
                      Payment Status
                      <p><span> PAID </span></p>
                    </div>
                  </div>
                </div>
                <div class="col-sm-4">
                  <div class="patient-detailed">
                    <div class="bill-add">Billing Address :</div>
                    <div class="add-details">
                      Walter Roberson <br />
                      299 Star Trek Drive, Panama City,<br />
                      Florida, 32405,<br />
                      USA
                    </div>
                  </div>
                </div>
                <div class="col-sm-4">
                  <div class="patient-detailed">
                    <div class="bill-add">Shipping Address :</div>
                    <div class="add-details">
                      Walter Roberson <br />
                      299 Star Trek Drive, Panama City,<br />
                      Florida, 32405,<br />
                      USA
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="invoice-table">
              <div class="table-responsive">
                <table>
                  <thead>
                    <tr class="ecommercetable">
                      <th class="table_width_1">#</th>
                      <th class="table_width_2">Item</th>
                      <th class="text-start">Quantity</th>
                      <th class="text-start">Unit Price</th>
                      <th class="text-start">Discount</th>
                      <th class="text-end">Amount</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>1</td>
                      <td class="text-start">Accounting Software Maintainence</td>
                      <td class="text-start">3</td>
                      <td class="text-start unit-price-data">
                        $500 <span>after disc. $450.00</span>
                      </td>
                      <td class="text-start">10%</td>
                      <td class="text-end">$1350</td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td class="text-start">Man Power Support</td>
                      <td class="text-start">1</td>
                      <td class="text-start unit-price-data">$100</td>
                      <td class="text-start">0%</td>
                      <td class="text-end">$100</td>
                    </tr>
                    <tr>
                      <td>3</td>
                      <td class="text-start">Transportation Fee</td>
                      <td class="text-start">2</td>
                      <td class="text-start unit-price-data">
                        $200 <span>after disc. $190.00</span>
                      </td>
                      <td class="text-start">5%</td>
                      <td class="text-end">$380</td>
                    </tr>
                    <tr>
                      <td>4</td>
                      <td class="text-start">Spars Replacement Charges</td>
                      <td class="text-start">5</td>
                      <td class="text-start unit-price-data">$500</td>
                      <td class="text-start">2%</td>
                      <td class="text-end">$2500</td>
                    </tr>
                    <tr>
                      <td>5</td>
                      <td class="text-start">Materials Handling</td>
                      <td class="text-start">2</td>
                      <td class="text-start unit-price-data">
                        $200 <span>after disc. $190.00</span>
                      </td>
                      <td class="text-start">5%</td>
                      <td class="text-end">$380</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="invoice-table-footer">
              <div class="table-footer-left notes">
                <div class="logo3">
                  <img src="@/assets/img/paid.svg" />
                </div>
              </div>
              <div class="text-end table-footer-right">
                <table>
                  <tbody>
                    <tr>
                      <td><span>Taxable Amount</span></td>
                      <td>$4705.00</td>
                    </tr>
                    <tr>
                      <td><span>IGST 18.0%</span></td>
                      <td>$846.90</td>
                    </tr>
                    <tr>
                      <td><span>Extra Discount (Promo - 5%)</span></td>
                      <td>$235.25</td>
                    </tr>
                    <tr>
                      <td><span>Round Off</span></td>
                      <td>-$.65</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="invoice-table-footer totalamount-footer">
              <div class="table-footer-left"></div>
              <div class="table-footer-right">
                <table class="totalamt-table">
                  <tbody>
                    <tr>
                      <td>Total Amount</td>
                      <td>$5316.00</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="total-amountdetails">
              <p>
                Total amount ( in words):
                <span> Five thousand three hundred and sixteen dollars only.</span>
              </p>
            </div>
            <div class="bank-details">
              <div class="row">
                <div class="col md-6">
                  <div class="payment-info">
                    <div class="qr">
                      <img src="@/assets/img/qr-code.svg" alt="qr" />
                      <h6 class="scan-details">Scan to View Receipt</h6>
                    </div>
                    <div class="pay-details">
                      <span class="payment-title">Payment Info:</span>
                      <div><span>Debit Card :</span> 465 *************645</div>
                      <div class="mb-0"><span>Amount :</span> $1,815</div>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="terms-condition">
                    <span>Terms & Conditions:</span>
                    <ol>
                      <li>Goods Once sold cannot be taken back or exchanged</li>
                      <li>
                        We are not the manufactures, company will stand for warrenty as
                        per their terms and conditions.
                      </li>
                    </ol>
                  </div>
                </div>
              </div>
            </div>

            <div class="thanks-msg text-center">Thanks for your Business</div>
          </div>
        </div>
        <div class="file-link">
          <button class="download_btn download-link">
            <i class="feather-download-cloud me-1"></i> <span>Download</span>
          </button>
          <a href="javascript:window.print()" class="print-link">
            <i class="feather-printer"></i> <span >Print</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
