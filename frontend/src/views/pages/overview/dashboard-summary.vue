<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Customer Details</h5>
        </div>
      </div>

      <!-- Customer Info Card -->
      <div class="card customer-details-group">
        <div class="card-body">
          <div class="row align-items-center">
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-img d-inline-flex" v-if="customer.profileImage">
                    <img class="rounded-circle" :src="customer.profileImage" alt="" />
                  </span>
                  <span class="customer-widget-icon" v-else>
                    <i class="feather feather-user rounded-circle"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>{{ customer.name }}</h6>
                    <p>{{ customer.customerId }}</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-icon">
                    <i class="feather feather-mail"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>Email Address</h6>
                    <p>{{ customer.email }}</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-icon">
                    <i class="feather feather-phone"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>Phone Number</h6>
                    <p>{{ customer.phone }}</p>
                  </div>
                </div>
              </div>
            </div>
            <div class="col-xl-3 col-lg-4 col-md-6 col-12">
              <div class="customer-details">
                <div class="d-flex align-items-center">
                  <span class="customer-widget-icon">
                    <i class="feather feather-map-pin"></i>
                  </span>
                  <div class="customer-details-cont">
                    <h6>Address</h6>
                    <p>{{ customer.address }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Account Summary Cards -->
      <div class="row">
        <div class="col-xl-3 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card account-card w-100">
            <div class="card-body">
              <div class="account-header">
                <span class="account-icon bg-primary-light">
                  <i class="feather feather-credit-card"></i>
                </span>
                <div class="account-details">
                  <h6>Total Balance</h6>
                  <h3>{{ formatCurrency(accountSummary.totalBalance) }}</h3>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-3 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card account-card w-100">
            <div class="card-body">
              <div class="account-header">
                <span class="account-icon bg-success-light">
                  <i class="feather feather-trending-up"></i>
                </span>
                <div class="account-details">
                  <h6>Total Deposits</h6>
                  <h3>{{ formatCurrency(accountSummary.totalDeposits) }}</h3>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-3 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card account-card w-100">
            <div class="card-body">
              <div class="account-header">
                <span class="account-icon bg-danger-light">
                  <i class="feather feather-trending-down"></i>
                </span>
                <div class="account-details">
                  <h6>Total Withdrawals</h6>
                  <h3>{{ formatCurrency(accountSummary.totalWithdrawals) }}</h3>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-3 col-lg-4 col-sm-6 col-12 d-flex">
          <div class="card account-card w-100">
            <div class="card-body">
              <div class="account-header">
                <span class="account-icon bg-warning-light">
                  <i class="feather feather-activity"></i>
                </span>
                <div class="account-details">
                  <h6>Active Accounts</h6>
                  <h3>{{ accountSummary.activeAccounts }}</h3>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Transaction History Table -->
      <div class="row">
        <div class="col-12">
          <div class="card">
            <div class="card-header">
              <h4>Transaction History</h4>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <a-table 
                  :columns="transactionColumns" 
                  :data-source="transactions"
                  :pagination="{ pageSize: 10 }"
                  :loading="loading"
                >
                  <template #bodyCell="{ column, record }">
                    <template v-if="column.key === 'type'">
                      <span :class="getTransactionTypeClass(record.type)">
                        {{ record.type }}
                      </span>
                    </template>
                    <template v-else-if="column.key === 'amount'">
                      <span :class="record.type === 'Credit' ? 'text-success' : 'text-danger'">
                        {{ formatCurrency(record.amount, record.currency) }}
                      </span>
                    </template>
                  </template>
                </a-table>
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const transactionColumns = [
  {
    title: "Date",
    dataIndex: "date",
    key: "date",
    sorter: true
  },
  {
    title: "Transaction ID",
    dataIndex: "transactionId",
    key: "transactionId"
  },
  {
    title: "Type",
    dataIndex: "type",
    key: "type",
    filters: [
      { text: 'Credit', value: 'Credit' },
      { text: 'Debit', value: 'Debit' }
    ]
  },
  {
    title: "Account",
    dataIndex: "account",
    key: "account"
  },
  {
    title: "Amount",
    dataIndex: "amount",
    key: "amount",
    sorter: true
  },
  {
    title: "Status",
    dataIndex: "status",
    key: "status"
  }
];

export default {
  setup() {
    const customer = ref({
      name: '',
      customerId: '',
      email: '',
      phone: '',
      address: '',
      profileImage: null
    })

    const accountSummary = ref({
      totalBalance: 0,
      totalDeposits: 0,
      totalWithdrawals: 0,
      activeAccounts: 0
    })

    const transactions = ref([])
    const loading = ref(true)

    const fetchUserProfile = async () => {
      try {
        const response = await axios.get('/api/v1/auth/profile')
        const profile = response.data
        customer.value = {
          name: `${profile.first_name} ${profile.last_name}`,
          customerId: profile.cif_number,
          email: profile.email,
          phone: profile.phone_number,
          address: [
            profile.address_line1,
            profile.address_line2,
            profile.address_line3,
            profile.address_line4
          ].filter(Boolean).join(', '),
          profileImage: null // Set default profile image path if needed
        }
      } catch (error) {
        console.error('Error fetching user profile:', error)
      }
    }

    const fetchAccountsAndTransactions = async () => {
      try {
        // Fetch accounts
        const accountsResponse = await axios.get('/api/v1/accounts')
        const accounts = accountsResponse.data

        // Calculate account summary
        let totalBalance = 0
        let totalDeposits = 0
        let totalWithdrawals = 0
        const activeAccounts = accounts.filter(acc => acc.status === 'active').length

        // Fetch balances and transactions
        const today = new Date()
        const lastMonth = new Date(today.setMonth(today.getMonth() - 1))

        const transactionPromises = accounts.map(async account => {
          // Get balance
          const balanceResponse = await axios.get(`/api/v1/accounts/${account.account_number}/balance`)
          totalBalance += parseFloat(balanceResponse.data.balance)

          // Get transactions
          const transactionsResponse = await axios.get(`/api/v1/accounts/${account.account_number}/transactions`, {
            params: {
              from_date: lastMonth.toISOString().split('T')[0],
              to_date: new Date().toISOString().split('T')[0]
            }
          })

          return transactionsResponse.data.map(tx => {
            if (tx.transaction_type === 'credit') {
              totalDeposits += parseFloat(tx.amount)
            } else {
              totalWithdrawals += parseFloat(tx.amount)
            }

            return {
              date: new Date(tx.transaction_date).toLocaleDateString(),
              transactionId: tx.reference,
              type: tx.transaction_type === 'credit' ? 'Credit' : 'Debit',
              account: account.account_number,
              amount: tx.amount,
              currency: tx.currency,
              status: tx.status
            }
          })
        })

        const transactionResults = await Promise.all(transactionPromises)
        transactions.value = transactionResults.flat()
          .sort((a, b) => new Date(b.date) - new Date(a.date))

        accountSummary.value = {
          totalBalance,
          totalDeposits,
          totalWithdrawals,
          activeAccounts
        }
      } catch (error) {
        console.error('Error fetching accounts and transactions:', error)
      } finally {
        loading.value = false
      }
    }

    const formatCurrency = (amount, currency = 'USD') => {
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: currency
      }).format(amount)
    }

    const getTransactionTypeClass = (type) => {
      return type === 'Credit' ? 'badge bg-success-light' : 'badge bg-danger-light'
    }

    onMounted(async () => {
      await fetchUserProfile()
      await fetchAccountsAndTransactions()
    })

    return {
      customer,
      accountSummary,
      transactions,
      transactionColumns,
      loading,
      getTransactionTypeClass,
      formatCurrency
    }
  }
}
</script>