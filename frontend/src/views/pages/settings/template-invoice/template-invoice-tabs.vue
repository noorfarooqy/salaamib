<template>
  <div class="card invoices-tabs-card">
    <div class="invoice-template-tab invoices-main-tabs">
      <div class="row align-items-center">
        <div class="col-lg-12">
          <div class="invoices-tabs">
            <ul class="nav nav-tabs">
              <li class="nav-item">
                <a
                  id="invoice-tab"
                  data-bs-toggle="tab"
                  data-bs-target="#invoice_tab"
                  type="button"
                  role="tab"
                  aria-controls="invoice_tab"
                  aria-selected="true"
                  href="javascript:void(0);"
                  class="active"
                  >Invoice</a
                >
              </li>
              <li class="nav-item">
                <a
                  id="purchases-tab"
                  data-bs-toggle="tab"
                  data-bs-target="#purchases_tab"
                  type="button"
                  role="tab"
                  aria-controls="purchases_tab"
                  aria-selected="true"
                  href="javascript:void(0);"
                  >Purchases
                </a>
              </li>
              <li class="nav-item">
                <a
                  id="receipt-tab"
                  data-bs-toggle="tab"
                  data-bs-target="#receipt_tab"
                  type="button"
                  role="tab"
                  aria-controls="receipt_tab"
                  aria-selected="true"
                  href="javascript:void(0);"
                  >Receipt
                </a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
