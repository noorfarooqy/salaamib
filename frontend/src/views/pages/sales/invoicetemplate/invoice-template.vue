<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="page-header">
        <div class="content-page-header">
          <h5>{{ title }}</h5>
        </div>
      </div>
      <!-- /Page Header -->
      <div class="card mb-0">
        <div class="card-body pb-0">
          <div class="invoice-card-title">
            <h6>General Invoice</h6>
          </div>
          <div class="row">
            <!-- Invoice List -->
            <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
              <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-betweens">
                <div class="blog-image">
                  <router-link to="invoice-one-a"><img class="img-fluid" src="@/assets/img/invoice-one.jpg"
                      alt="Post Image" />
                  </router-link>
                </div>
                <div class="invoice-content-title">
                  <router-link to="invoice-one-a">General Invoice 1</router-link>
                </div>
              </div>
            </div>
            <!-- /Invoice List -->
            <!-- Invoice List -->
            <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
              <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-between">
                <div class="blog-image">
                  <router-link to="invoice-two"><img class="img-fluid" src="@/assets/img/invoice-two.jpg"
                      alt="Post Image" />
                  </router-link>
                </div>
                <div class="invoice-content-title">
                  <router-link to="invoice-two"> General Invoice 2 </router-link>
                </div>
              </div>
            </div>
            <!-- /Invoice List -->
            <!-- Invoice List -->
            <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
              <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-between">
                <div class="blog-image">
                  <router-link to="invoice-three"><img class="img-fluid" src="@/assets/img/invoice-three.jpg"
                      alt="Post Image" />
                  </router-link>
                </div>
                <div class="invoice-content-title">
                  <router-link to="invoice-three"> General Invoice 3 </router-link>
                </div>
              </div>
            </div>
            <!-- /Invoice List -->
            <!-- Invoice List -->
            <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
              <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-between">
                <div class="blog-image">
                  <router-link to="invoice-four-a"><img class="img-fluid" src="@/assets/img/invoice-four.jpg"
                      alt="Post Image" />
                  </router-link>
                </div>
                <div class="invoice-content-title">
                  <router-link to="invoice-four-a"> General Invoice 4 </router-link>
                </div>
              </div>
            </div>
            <!-- Invoice List -->
            <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
              <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-between">
                <div class="blog-image">
                  <router-link to="invoice-five"><img class="img-fluid" src="@/assets/img/invoice-five.jpg"
                      alt="Post Image" />
                  </router-link>
                </div>
                <div class="invoice-content-title">
                  <router-link to="invoice-five"> General Invoice 5 </router-link>
                </div>
              </div>
            </div>
            <!-- /Invoice List -->
            <!-- /Invoice List -->
          </div>
          <div class="row">
            <!-- /Invoice List -->
            <div class="row">
              <div class="invoice-card-title">
                <h6>Receipt Invoice</h6>
              </div>
              <!-- Invoice List -->
              <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
                <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-between">
                  <div class="blog-image">
                    <router-link to="cashreceipt-1"><img class="img-fluid" src="@/assets/img/cash-receipt-1.svg"
                        alt="Post Image" />
                    </router-link>
                  </div>
                  <div class="invoice-content-title">
                    <router-link to="cashreceipt-1"> Cash Receipt 1 </router-link>
                  </div>
                </div>
              </div>
              <!-- /Invoice List -->
              <!-- Invoice List -->
              <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
                <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-between">
                  <div class="blog-image">
                    <router-link to="cashreceipt-2"><img class="img-fluid" src="@/assets/img/cash-receipt-2.svg"
                        alt="Post Image" />
                    </router-link>
                  </div>
                  <div class="invoice-content-title">
                    <router-link to="cashreceipt-2"> Cash Receipt 2 </router-link>
                  </div>
                </div>
              </div>
              <!-- /Invoice List -->
              <!-- Invoice List -->
              <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
                <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-between">
                  <div class="blog-image">
                    <router-link to="cashreceipt-3"><img class="img-fluid" src="@/assets/img/cash-receipt-3.svg"
                        alt="Post Image" />
                    </router-link>
                  </div>
                  <div class="invoice-content-title">
                    <router-link to="cashreceipt-3"> Cash Receipt 3 </router-link>
                  </div>
                </div>
              </div>
              <!-- /Invoice List -->
              <!-- Invoice List -->
              <div class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
                <div class="blog grid-blog flex-fill d-flex flex-wrap align-content-between">
                  <div class="blog-image">
                    <router-link to="cashreceipt-4"><img class="img-fluid" src="@/assets/img/cash-receipt-4.svg"
                        alt="Post Image" />
                    </router-link>
                  </div>
                  <div class="invoice-content-title">
                    <router-link to="cashreceipt-4"> Cash Receipt 4 </router-link>
                  </div>
                </div>
              </div>
              <!-- /Invoice List -->
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
      title: "Invoice Template",
    };
  },
};
</script>
