<template>
  <div class="no-stickybar">
    <div class="main-wrapper invoice-two">
      <div class="container">
        <div class="invoice-wrapper download_section">
          <div class="inv-content invoice-two">
            <div class="invoice-header">
              <div class="inv-header-left">
                <h2>Invoice</h2>
              </div>
              <div class="inv-header-right">
                <a href="javascript:;">
                  <img src="@/assets/img/logo2.png" alt="Logo" />
                </a>
              </div>
            </div>
            <div class="two-invoice-details">
              <div class="company-booking-address">
                <div class="company-add">
                  Dreams Technologies PVT Ltd
                  <span>Address: 15 Hodges Mews,High Wycomb HP123JL,United Kingdom</span>
                </div>
                <div class="invoice-date">
                  <h6>Invoice No :<span>#005</span></h6>
                  <h6>Invoice Date :<span> 07-10-2023</span></h6>
                </div>
              </div>
              <h5>Customer Info</h5>
              <div class="invoice-address-details">
                <div class="container">
                  <div class="row">
                    <div class="col-sm-4">
                      <div class="invoice-to">
                        <span>Invoice To :</span>
                        <div class="inv-to-address">
                          Walter Roberson<br />
                          299 Star Trek Drive, Panama City, <br />
                          Florida, 32405,<br />
                          USA.
                        </div>
                      </div>
                    </div>
                    <div class="col-sm-4">
                      <div class="invoice-to">
                        <span>Pay To :</span>
                        <div class="inv-to-address">
                          Walter Roberson<br />
                          299 Star Trek Drive, Panama City, <br />
                          Florida, 32405, <br />
                          USA.
                        </div>
                      </div>
                    </div>
                    <div class="col-sm-4">
                      <div class="invoice-to-payment">
                        <span>Due Date</span>
                        <div class="inv-to-address">
                          <h6>07/23/2023</h6>
                          <br />
                          <span>Payment Status</span><br />
                          NOT PAID<br />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="invoice-table-details">
                <div class="table-responsive">
                  <table>
                    <thead>
                      <tr class="ecommercetable">
                        <th class="table_width_1">#</th>
                        <th class="table_width_1">Item</th>
                        <th class="table_width_1">Quantity</th>
                        <th class="text-start">Unit Price</th>
                        <th class="text-start">Discount</th>
                        <th class="text-end">Amount</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <td>1</td>
                        <td class="table-description">
                          Accounting Software Maintainence
                        </td>
                        <td class="text-start">3</td>
                        <td class="text-start">
                          $500
                          <h6>after disc. $450.00</h6>
                        </td>
                        <td class="text-start">10%</td>
                        <td class="text-end">$1350</td>
                      </tr>
                      <tr>
                        <td>2</td>
                        <td class="table-description">Man Power Support</td>
                        <td >1</td>
                        <td >$100</td>
                        <td >0%</td>
                        <td class="text-end">$100</td>
                      </tr>
                      <tr>
                        <td>3</td>
                        <td class="table-description">Transportation Fee</td>
                        <td >2</td>
                        <td >
                          $200
                          <h6>after disc. $450.00</h6>
                        </td>
                        <td >5%</td>
                        <td class="text-end">$380</td>
                      </tr>
                      <tr>
                        <td>4</td>
                        <td class="table-description">Spars Replacement Charges</td>
                        <td >5</td>
                        <td >$500</td>
                        <td >0%</td>
                        <td class="text-end">$2500</td>
                      </tr>
                      <tr>
                        <td>5</td>
                        <td class="table-description">Materials Handling</td>
                        <td >1</td>
                        <td >
                          $500
                          <h6>after disc. $450.00</h6>
                        </td>
                        <td >25%</td>
                        <td class="text-end">$375</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
              <div class="invoice-table-footer">
                <div class="table-footer-left notes"></div>
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
            </div>
            <div class="bank-details">
              <div class="container">
                <div class="row">
                  <div class="col-md-6">
                    <div class="payment-info">
                      <div class="qr-code">
                        <img src="@/assets/img/qr-code.svg" alt="qr" />
                        <h6 class="scan-details">Scan to View Receipt</h6>
                      </div>
                      <div class="debitcard">
                        <span class="payment-title">Payment Info:</span>
                        <div class="debit-card">
                          <span>Debit Card :</span> 465 *************645
                        </div>
                        <div class="mb-0"><span>Amount :</span> $1,815</div>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="terms-condition">
                      <div class="amount">
                        Total amount (in word):Five thousand three hundred and sixteen
                        dollars only.
                      </div>
                      <span>Terms & Conditions:</span>
                      <ol>
                        <li>
                          This is a GST based invoice bill,Which is applicable for TDS
                          Deduction
                        </li>
                        <li>
                          We are not the manufactures, company will stand for warranty as
                          per their terms and conditions.
                        </li>
                      </ol>
                    </div>
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
