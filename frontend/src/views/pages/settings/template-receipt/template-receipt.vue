<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->

      <!-- /Page Header -->

      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar />
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="w-100 pt-0">
            <div class="content-page-header">
              <h5>Receipt Templates</h5>
            </div>
            <div class="card template-invoice-card mb-0">
              <div class="card-body pb-0">
                <div class="invoice-card-title">
                  <h6>Receipt</h6>
                </div>
                <div class="row">
                  <!-- Invoice List -->
                  <div v-for="item in templateReceipt" :key="item.id"
                    class="col-md-6 col-xl-3 col-sm-12 d-md-flex d-sm-block">
                    <div class="blog grid-blog invoice-blog flex-fill d-flex flex-wrap align-content-between">
                      <div class="blog-image">
                        <router-link :to="item.href" class="img-general" data-bs-toggle="modal"
                          :data-bs-target="item.data_bs_target"><img class="img-fluid"
                            :src="require(`@/assets/img/${item.imgSrc}`)" alt="Post Image" />
                        </router-link>
                        <a href="javascript:;" class="preview-invoice"><i class="fa-regular fa-eye"></i></a>
                      </div>
                      <div class="invoice-content-title">
                        <router-link :to="item.href">{{
                          item.invoiceTitle
                        }}</router-link>
                        <span class="invoice-star" data-bs-toggle="tooltip" data-bs-placement="left" title=""
                          data-bs-original-title="Make as default"><i class="fa-regular fa-star"></i></span>
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
    </div>
  </div>
  <receipt-invoice></receipt-invoice>
</template>
<script>
import templateReceipt from "@/assets/json/template-receipt";
export default {
  setup() {
    return {
      templateReceipt: templateReceipt,
    };
  },
};
</script>
