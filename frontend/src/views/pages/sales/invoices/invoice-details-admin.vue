<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="card">
        <div class="card-body">
          <div class="page-header">
            <div class="content-invoice-header">
              <h5>Invoice Details</h5>
            </div>
          </div>
          <!-- /Page Header -->
          <div class="row justify-content-center">
            <div class="col-lg-8">
              <div class="cards">
                <div class="card-bod">
                  <div class="card-table">
                    <div class="card-bod">
                      <!-- Invoice Logo -->
                      <div class="invoice-item invoice-item-one">
                        <div class="row align-items-center">
                          <div class="col-md-6">
                            <div class="invoice-logo">
                              <img src="@/assets/img/logo.png" alt="logo" />
                            </div>
                          </div>
                          <div class="col-md-6">
                            <div class="invoice-info">
                              <h1 class="text-warning">UNPAID</h1>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!-- /Invoice Logo -->

                      <!-- Invoice Date -->
                      <div class="invoice-item invoice-item-date">
                        <div class="row">
                          <div class="col-md-6">
                            <p class="text-start invoice-details">
                              Issue Date<span>: </span><strong>13 Apr 2023</strong>
                            </p>
                          </div>
                          <div class="col-md-6">
                            <p class="text-start invoice-details">
                              Due Date<span>: </span><strong>03 Jun 2023</strong><span class="text-danger">Due in 8
                                days</span>
                            </p>
                          </div>
                          <!-- <div class="col-md-4">
																<p class="invoice-details">
																	Invoice No<span>: </span><strong>INV 00001</strong> 
																</p>
															</div> -->
                        </div>
                      </div>
                      <!-- /Invoice Date -->

                      <!-- Invoice To -->
                      <div class="invoice-item invoice-item-two">
                        <div class="row">
                          <div class="col-md-6">
                            <div class="invoice-info">
                              <strong class="customer-text-one">Invoiced To<span>:</span></strong>
                              <p class="invoice-details-two">
                                John Williams<br />
                                15 Hodges Mews, High Wycombe<br />
                                HP12 3JL<br />
                                United Kingdom
                              </p>
                            </div>
                          </div>
                          <div class="col-md-6">
                            <div class="invoice-info invoice-info2">
                              <strong class="customer-text-one">Pay To<span>:</span></strong>
                              <p class="invoice-details-two">
                                Walter Roberson<br />
                                299 Star Trek Drive, Panama City,<br />
                                Florida, 32405,<br />
                                USA
                              </p>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!-- /Invoice To -->

                      <!-- Invoice Item -->
                      <div class="invoice-item invoice-table-wrap">
                        <div class="invoice-table-head">
                          <h6>Items:</h6>
                        </div>
                        <div class="row">
                          <div class="col-md-12">
                            <div class="table-responsive">
                              <table class="table table-center table-hover mb-0">
                                <thead class="thead-light">
                                  <tr>
                                    <th>Product / Service</th>
                                    <th>Quantity</th>
                                    <th>Unit</th>
                                    <th>Rate</th>
                                    <th>Discount</th>
                                    <th>Tax</th>
                                    <th>Amount</th>
                                  </tr>
                                </thead>
                                <tbody>
                                  <tr>
                                    <td>Lorem ipsum dolor sit amet</td>
                                    <td>1</td>
                                    <td>Pcs</td>
                                    <td>$120.00</td>
                                    <td>0</td>
                                    <td>0</td>
                                    <td>$120.00</td>
                                  </tr>
                                  <tr>
                                    <td>Lorem ipsum dolor sit amet</td>
                                    <td>1</td>
                                    <td>Pcs</td>
                                    <td>$210.00</td>
                                    <td>0</td>
                                    <td>0</td>
                                    <td>$210.00</td>
                                  </tr>
                                  <tr>
                                    <td>Lorem ipsum dolor sit amet</td>
                                    <td>1</td>
                                    <td>Pcs</td>
                                    <td>$310.00</td>
                                    <td>0</td>
                                    <td>0</td>
                                    <td>$310.00</td>
                                  </tr>
                                </tbody>
                              </table>
                            </div>
                          </div>
                        </div>
                      </div>
                      <!-- /Invoice Item -->
                      <div class="col-lg-12 col-md-12">
                        <div class="invoice-total-card">
                          <div class="invoice-total-box">
                            <div class="invoice-total-inner">
                              <p>Taxable <span>$360.00</span></p>
                              <p>Discount<span>$13.20</span></p>
                              <p>Vat <span>$0.00</span></p>
                            </div>
                            <div class="invoice-total-footer">
                              <h4>Total Amount <span>$347.80</span></h4>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-lg-4">
              <div class="card timeline-card">
                <div class="card-body">
                  <div class="form-group">
                    <label>Status</label>
                    <vue-select :options="Paid" id="Paid" placeholder="Paid" />
                  </div>
                  <div class="invoice-info invoice-info2 admin-invoice invoice-item mb-4">
                    <strong class="customer-text-one mt-3">Payment Details<span>:</span></strong>
                    <p class="text-start invoice-details-two invoice-details mb-2">
                      PayPal :<strong>examplepaypal.co</strong>
                    </p>
                    <p class="text-start invoice-details-two invoice-details mb-2">
                      Account :<strong>examplepaypal.co</strong>
                    </p>
                    <p class="text-start invoice-details-two invoice-details">
                      Payment Term :
                    </p>
                    <div class="due-date">
                      <strong>15 days</strong><span class="text-danger">Due in 8 days</span>
                    </div>
                  </div>
                  <strong class="customer-text-one">Timeline<span>:</span></strong>
                  <ul class="activity-feed">
                    <li class="feed-item timeline-item">
                      <span class="feed-text timeline-user"><router-link to="/profile">John Smith</router-link> Created
                        Invoice</span>
                      <div class="invoice-date">
                        <span class="start-date">07 April 2023</span><span>07 April 2023</span>
                      </div>
                    </li>
                    <li class="feed-item timeline-item">
                      <span class="feed-text timeline-user"><router-link to="/profile">John Smith</router-link> Created
                        Invoice</span>
                      <div class="invoice-date">
                        <span class="start-date">07 April 2023</span><span>07 April 2023</span>
                      </div>
                    </li>
                    <li class="feed-item timeline-item">
                      <span class="feed-text timeline-user"><router-link to="/profile">John Smith</router-link> Created
                        Invoice</span>
                      <div class="invoice-date">
                        <span class="start-date">07 April 2023</span><span>07 April 2023</span>
                      </div>
                    </li>
                    <li class="feed-item timeline-item">
                      <span class="feed-text timeline-user"><router-link to="/profile">John Smith</router-link> Created
                        Invoice</span>
                      <div class="invoice-date">
                        <span class="start-date">07 April 2023</span><span>07 April 2023</span>
                      </div>
                    </li>
                    <li class="feed-item timeline-item">
                      <span class="feed-text timeline-user"><router-link to="/profile">John Smith</router-link> Created
                        Invoice</span>
                      <div class="invoice-date">
                        <span class="start-date">07 April 2023</span><span>07 April 2023</span>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="terms-conditions">
              <div class="row align-items-center justify-content-between">
                <div class="col-lg-6 col-md-6">
                  <div class="invoice-terms align-center justify-content-start">
                    <span class="invoice-terms-icon bg-white-smoke me-3">
                      <i class="feather feather-file-text"></i>
                    </span>
                    <div class="invocie-note">
                      <h6>Terms & Conditions</h6>
                      <p class="mb-0">
                        Authoritatively envisioneer business action items through
                        parallel sources.
                      </p>
                    </div>
                  </div>
                  <div class="invoice-terms align-center justify-content-start">
                    <span class="invoice-terms-icon bg-white-smoke me-3">
                      <i class="feather feather-file-minus"></i>
                    </span>
                    <div class="invocie-note">
                      <h6>Note</h6>
                      <p class="mb-0">
                        This is computer generated receipt and does not require physical
                        signature.
                      </p>
                    </div>
                  </div>
                </div>
                <div class="invoice-sign text-end col-lg-6">
                  <span class="d-block">Authorised Sign</span>
                  <img class="img-fluid d-inline-block light-color-logo" src="@/assets/img/signature.png" alt="sign" />
                  <img class="img-fluid d-inline-block dark-white-logo" src="@/assets/img/signature-white.png"
                    alt="sign" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      Paid: [
        "Paid",
        "Unpaid",
        "Partially paid",
        "Overdue",
        "Cancelled",
        "Refunded",
        "Draft",
      ],
    };
  },
};
</script>
