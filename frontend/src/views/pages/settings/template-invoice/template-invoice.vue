<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <!-- Page Header -->
      <div class="row">
        <div class="col-xl-3 col-md-4">
          <settingsidebar />
        </div>
        <div class="col-xl-9 col-md-8">
          <div class="w-100 pt-0">
            <div class="content-page-header">
              <h5>Invoice Templates</h5>
            </div>
            <!-- All Invoice -->
            <template-invoice-tabs></template-invoice-tabs>
            <div class="tab-content">
              <div class="tab-pane active" id="invoice_tab" role="tabpanel" aria-labelledby="invoice-tab" tabindex="0">
                <invoice></invoice>
              </div>
              <div class="tab-pane" id="purchases_tab" role="tabpanel" aria-labelledby="purchases-tab" tabindex="0">
                <purchase></purchase>
              </div>
              <div class="tab-pane" id="receipt_tab" role="tabpanel" aria-labelledby="receipt-tab" tabindex="0">
                <receipt></receipt>
              </div>
            </div>
            <!-- /All Invoice -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
