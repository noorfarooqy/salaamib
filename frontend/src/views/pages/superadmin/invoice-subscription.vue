<template>
  <div class="no-stickybar">
    <div class="main-wrapper">
      <div class="container">
        <div class="invoice-wrapper download_section subscription-invoice">
          <div class="inv-content">
            <div class="invoice-header">
              <div class="inv-header-right text-start">
                <a href="#">
                  <img class="logo-lightmode" src="@/assets/img/logo2.png" alt="Logo" />
                  <img
                    class="logo-darkmode"
                    src="@/assets/img/logo2-white.png"
                    alt="Logo"
                  />
                </a>
                <span>Original For Recipient</span>
              </div>
              <div class="inv-header-left">
                <h4>Subscription INVOICE</h4>
                <div class="invoice-num-date">
                  <ul>
                    <li>Date : <span>05/01/2024</span></li>
                    <li>Invoice No : <span>INV00001</span></li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="patient-infos">
              <div class="row">
                <div class="col-lg-6">
                  <div class="row">
                    <div class="col-sm-7">
                      <div class="sub-invoive-detail">
                        <h5>Invoice To :</h5>
                        <p>
                          Hellman-Ullrich <br />
                          299 Star Trek Drive, Panama City,<br />
                          Florida, 32405, USA.<br />
                          info@gmail.com<br />
                          +45 5421 4523
                        </p>
                      </div>
                    </div>
                    <div class="col-sm-5">
                      <div class="sub-invoive-detail">
                        <h5>Pay To :</h5>
                        <p>
                          Kanakku<br />
                          84 Spilman Street, London<br />
                          United King<br />
                          domlowell@gmail.com<br />
                          +45 5421 2154
                        </p>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-lg-6">
                  <div class="sub-invoive-detail detail-right">
                    <h5>Kanakku</h5>
                    <ul>
                      <li>GST IN :<br />22AABCU9603R1ZX</li>
                      <li>
                        Address :<br />15 Hodges Mews, High Wycombe HP12 3JL, United
                        Kingdom.
                      </li>
                      <li>Mobile :<br />+91 98765 43210</li>
                    </ul>
                  </div>
                </div>
              </div>
            </div>
            <div class="invoice-table p-0">
              <div class="table-responsive">
                <table>
                  <thead>
                    <tr class="ecommercetable">
                      <th class="table_width_1">#</th>
                      <th class="table_width_2">Item</th>
                      <th class="text-start">Tax Value</th>
                      <th class="text-end">Qty</th>
                      <th class="text-end">Price</th>
                      <th class="text-end">Total</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>1</td>
                      <td class="text-start">Basic Plan</td>
                      <td class="text-start">Monthly Package</td>
                      <td class="text-end unit-price-data">1</td>
                      <td class="text-end">$350</td>
                      <td class="text-end">$350</td>
                    </tr>
                    <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td class="text-end">
                        IGST 18.0% <br /><span class="mt-2 d-inline-flex">Sub Total</span>
                      </td>
                      <td class="text-end">
                        $165.00 <br /><span class="mt-2 d-inline-flex">$455.00</span>
                      </td>
                    </tr>
                    <tr>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td></td>
                      <td class="text-end">
                        <h4>Total</h4>
                      </td>
                      <td class="text-end">
                        <h4>$455.00</h4>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="total-amountdetails ps-0 pe-0">
              <p>
                Total amount ( in words): <span> USD Four Hundred and Fifty Five</span>
              </p>
            </div>
            <div class="bank-details p-0">
              <div class="row w-100 align-items-center">
                <div class="col md-6">
                  <div class="payment-info">
                    <div class="qr">
                      <h5>Bank Details</h5>
                    </div>
                    <div class="pay-details">
                      <div class="mb-2">
                        <span class="payment-title">Bank : YES Bank</span>
                      </div>
                      <div class="mb-2"><span>Account # : 6677889944551 </span></div>
                      <div class="mb-2"><span>IFSC : YESBBIN4567 </span></div>
                      <span>BRANCH : UK</span>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="company-sign">
                    <span>For Kanakku</span>
                    <img src="@/assets/img/signature.png" alt="signature-img" />
                  </div>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col-md-12">
                <div class="terms-condition p-0">
                  <span>Terms & Conditions:</span>
                  <ol>
                    <li>Goods Once sold cannot be taken back or exchanged</li>
                    <li>
                      We are not the manufactures, company will stand for warrenty as per
                      their terms and conditions.
                    </li>
                  </ol>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="file-link justify-content-center subscription-invoice-foot">
          <button class="download_btn download-link">
            <i class="feather-download-cloud me-1"></i> <span>Download</span>
          </button>
          <a href="javascript:window.print()" class="print-link">
            <i class="feather-printer"></i> <span class="">Print</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>
