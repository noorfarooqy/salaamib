<template>
  <div class="no-stickybar">
    <div class="main-wrapper invoice-three">
      <div class="container">
        <div class="invoice-wrapper download_section">
          <div class="inv-content">
            <div class="invoice-header">
              <div class="inv-header-left">
                <div class="invoice-title tax-invoice">INVOICE</div>
                <div class="company-details">
                  <span class="company-name invoice-title">Dreams</span>
                  <div class="gst-details">GST IN : <span>22AABCU9603R1ZX</span></div>
                  <div class="gst-details">
                    Address :
                    <span>5 Hodges Mews, High Wycombe HP12 3JL, United Kingdom</span>
                  </div>
                  <div class="gst-details mb-0">
                    Mobile : <span>+ 91 98765 43210</span>
                  </div>
                </div>
              </div>
              <div class="inv-header-right">
                <a href="javascript:;">
                  <img src="@/assets/img/logo2.png" alt="Logo" />
                </a>
              </div>
            </div>
            <div class="invoice-address">
              <div class="invoice-address-details">
                <div class="invoice-to">
                  <span>Billing Address:</span>
                  <div class="inv-to-address">
                    Walter Roberson<br />
                    299 Star Trek Drive, Panama City, <br />
                    Florida, 32405, USA.<br />
                    walter@example.com <br />
                    +45 5421 4523
                  </div>
                </div>
                <div class="invoice-to">
                  <span>Shipping Address:</span>
                  <div class="inv-to-address">
                    Lowell H. Dominguez<br />
                    84 Spilman Street, London<br />
                    United King<br />
                    domlowell@example.com<br />
                    +45 5421 2154
                  </div>
                </div>
              </div>
              <div class="invoice-details-content">
                <div class="invoice-status-details">
                  <div>
                    <span>Invoice No:</span>
                    <span>#10077005</span>
                  </div>
                </div>
                <div class="invoice-status-details">
                  <div>
                    <span>Invoice Date:</span>
                    <span>07/12/2023</span>
                  </div>
                </div>
                <div class="invoice-status-details">
                  <div>
                    <span>Payment Status:</span>
                    <span>NOT PAID</span>
                  </div>
                </div>
                <div class="invoice-status-details">
                  <div>
                    <span>Due Date :</span>
                    <span>07/31/2023</span>
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
              <div class="table-footer-left notes"></div>
              <div class="text-end table-footer-right">
                <table>
                  <tbody>
                    <tr>
                      <td class="table-footer-right-title">Taxable Amount</td>
                      <td>$18,218.00</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="invoice-table-footer">
              <div class="table-footer-left notes">
                <span></span>
              </div>
              <div class="text-end table-footer-right">
                <table>
                  <tbody>
                    <tr>
                      <td class="table-footer-right-title">IGST 18.0%</td>
                      <td>$3,279.00</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="invoice-table-footer">
              <div class="table-footer-left notes">
                <span></span>
              </div>
              <div class="text-end table-footer-right">
                <table>
                  <tbody>
                    <tr>
                      <td class="table-footer-right-title">
                        Extra Discount (Promo - 5%)
                      </td>
                      <td>-$235.25</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="invoice-table-footer">
              <div class="table-footer-left notes">
                <span></span>
              </div>
              <div class="text-end table-footer-right">
                <table>
                  <tbody>
                    <tr>
                      <td class="table-footer-right-title">Round Off</td>
                      <td>-$.65</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="invoice-table-footer mt-4">
              <div class="table-footer-left">
                <span class="total-item">Total amount (in words):</span>
                <span>Five thousand three hundred and sixteen dollars only.</span>
              </div>
              <div class="text-end table-footer-right">
                <table>
                  <tbody>
                    <tr>
                      <td class="invoice-title">Amount Payable</td>
                      <td class="invoice-title">$5,316.00</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <div class="bank-details">
              <div class="account-info">
                <div>
                  <span class="bank-title">Bank Details</span>
                  <div class="account-details">Bank : <span>YES Bank</span></div>
                  <div class="account-details">
                    Account # :<span> 6677889944551 </span>
                  </div>
                  <div class="account-details">IFSC : <span>YESBBIN4567</span></div>
                  <div class="account-details">BRANCH : <span>Florida</span></div>
                </div>
                <div class="qr-code">
                  <img src="@/assets/img/qr-code.svg" alt="qr" />
                  <p class="scan-details">Scan to View Receipt</p>
                </div>
              </div>
              <div class="company-sign">
                <span>For Dreams</span>
                <img src="@/assets/img/signature.png" alt="signature-img" />
              </div>
            </div>
            <div class="invoice-notes">
              <p>
                <strong
                  >NOTES: All accounts are to be paid within 7 days from receipt of
                  invoice. To be paid by cheque or credit card or direct payment online.
                  If account is not paid within 7 days the credits details supplied as
                  confirmation of work undertaken will be charged the agreed quoted fee
                  noted above.</strong
                >
              </p>
            </div>
            <div class="thanks-msg text-start">Thanks for your Business</div>
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
